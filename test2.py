from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import argparse

def check_replication_status(shard_ports):
    print("\n--- СТАТУС РЕПЛИКАЦИИ")
    
    for shard, ports in shard_ports.items():
        print(f"\nПроверка сегмента {shard}:")
        try:
            # Подключение 
            client = MongoClient(f'mongodb://localhost:{ports[0]}')
            status = client.admin.command({'replSetGetStatus': 1})
            
            # Проверка наличия PRIMARY
            members = status['members']
            primary = [m for m in members if m['stateStr'] == 'PRIMARY']
            if not primary:
                raise Exception(f"Нет PRIMARY узла в сегменте {shard}")
            
            # Проверка состояния всех узлов
            for member in members:
                state = member['state']
                health = member['health']
                if state not in [1, 2]:
                    if health != 1:
                        raise Exception(f"Некорректное состояние узла {member['name']}: {state}")
                print(f"- {member['name']}: Реплика-сет в норме")
            
        except Exception as e:
            print(f"Ошибка в {shard}: {str(e)}")


def check_cluster_status(client):
    print("\n--- СТАТУС КЛАСТЕРА")
    
    try:
        # Получение информации о балансировщике
        balancer_status = client.admin.command({'balancerStatus': 1})
        print("\nБалансировщик:")
        print(f"- Состояние: {'активен' if balancer_status['mode'] == 'full' else 'отключен'}")
        print(f"- В процессе работы: {balancer_status['inBalancerRound']}")
        print(f"- Последняя ошибка: {balancer_status.get('errmsg', 'нет')}")

        # Настройки autosplit и automerge
        settings = client.config.settings.find_one({'_id': 'autosplit'})
        if settings:
            print("\nAutoSplit:")
            print(f"- Включен: {not settings.get('enabled', True)}")
        else:
            print("\nAutoSplit: используется значение по умолчанию (включен)")

        merge_settings = client.config.settings.find_one({'_id': 'automerge'})
        if merge_settings:
            print("\nAutoMerge:")
            print(f"- Включен: {merge_settings.get('enabled', True)}")
        else:
            print("\nAutoMerge: используется значение по умолчанию (включен)")

        # Распределение чанков
        chunks = client.config.chunks.aggregate([
            {"$group": {"_id": "$shard", "count": {"$sum": 1}}}
        ])
        print("\nРаспределение чанков:")
        for chunk in chunks:
            print(f"- {chunk['_id']}: {chunk['count']} чанков")
    
    except OperationFailure as e:
        print(f"Ошибка: {e.details['errmsg']}")
    except Exception as e:
        print(f"Общая ошибка: {str(e)}")


def check_data_distribution(client, collection_name, shard_ports):
    try:
        # Получаем UUID коллекции
        coll_info = client.config.collections.find_one({
            "_id": f"testDB.{collection_name}"
        })

        collection_uuid = coll_info.get('uuid', None)
        if not collection_uuid:
            print("Не удалось получить UUID коллекции")
            return

        # Ищем чанки по UUID коллекции
        chunks = list(client.config.chunks.find({
            "uuid": collection_uuid
        }))

        if not chunks:
            print(f"Не найдено чанков для коллекции {collection_name}")
            print("Возможные причины:")
            print("- Данные еще не были распределены")
            print("- Коллекция пустая")
            return

        # Группируем чанки по шардам
        shard_distribution = {}
        for chunk in chunks:
            shard = chunk.get('shard', 'unknown')
            if shard not in shard_distribution:
                shard_distribution[shard] = {
                    'chunks': 0,
                    'ranges': []
                }
            shard_distribution[shard]['chunks'] += 1
            shard_distribution[shard]['ranges'].append({
                'min': chunk.get('min', {}),
                'max': chunk.get('max', {})
            })

        # Собираем общую информацию
        coll_stats = client["testDB"].command('collStats', collection_name)
        total_data = coll_stats.get('size', 0)
        total_docs = coll_stats.get('count', 0)

        # Собираем информацию посегментно
        total_chunks = 0
        shard_stats = {}
        for shard, data in shard_distribution.items():
            conn = MongoClient(f'mongodb://localhost:{shard_ports.get(shard)[0]}')
            stats = conn["testDB"].command('collStats', collection_name)
        
            shard_stats[shard] = {
                'data_size': stats.get('size', 0),
                'doc_count': stats.get('count', 0)
            }
            total_chunks += data['chunks']

        # Выводим результаты
        print(f"\nДля {collection_name}:")

        for shard, data in shard_distribution.items():
            stats = shard_stats.get(shard, {})
            ports = ", ".join(map(str, shard_ports.get(shard, [])))
            print(f"\nСегмент: {shard}")
            print(f"- Порты: {ports}")
            print(f"- Чанков: {data['chunks']}")
            
            if data['ranges']:
                if len(data['ranges']) > 1:
                    print("\n- Границы первого чанка:")
                    print(f"  Min: {data['ranges'][0]['min']}")
                    print(f"  Max: {data['ranges'][0]['max']}")
                    print("\n- Границы последнего чанка:")
                    print(f"  Min: {data['ranges'][-1]['min']}")
                    print(f"  Max: {data['ranges'][-1]['max']}")
                else:
                    print("\n- Границы чанка:")
                    print(f"  Min: {data['ranges'][0]['min']}")
                    print(f"  Max: {data['ranges'][0]['max']}")
                
                if stats:
                    data_mb = stats['data_size'] / (1024 ** 2)
                    print(f"\n- Данные : {data_mb:.2f}MiB")
                    print(f"- Документы : {stats['doc_count']}")
                    if total_chunks > 0:
                        avg_data = stats['data_size'] / total_chunks / (1024 ** 2)
                        avg_docs = stats['doc_count'] / total_chunks
                        print(f"- Объем данных на чанк: {avg_data:.2f}MiB")
                        print(f"- Объем документов на чанк: {avg_docs:.1f}")

        if total_data > 0:
            total_mb = total_data / (1024 ** 2)
            print(f"\nВсего данных: {total_mb:.2f}MiB")
            print(f"Всего документов: {total_docs}\n")
            
            # Расчет процентов
            for shard, data in shard_distribution.items():
                stats = shard_stats.get(shard, {})
                data_percent = (stats['data_size'] / total_data) * 100
                docs_percent = (stats['doc_count'] / total_docs) * 100 if total_docs > 0 else 0
                print(f"Сегмент {shard} содержит {data_percent:.1f}% данных, {docs_percent:.1f}% документов колекции {collection_name} в кластере")

    except OperationFailure as e:
        print(f"Ошибка MongoDB: {e.details['errmsg']}")
    except Exception as e:
        print(f"Общая ошибка: {str(e)}")


def check_queries(client):
    print("\n--- ПРОВЕРКА ЗАПРОСОВ")
    
    try:
        # Запрос к хеш-сегментированной коллекции
        print("\nЗапрос к users_hash:")
        result_hash = client.testDB.users_hash.find_one({"userId": 42})
        print(f"- Имя из документа с userId = 42: {result_hash['name']}" if result_hash else "Документ не найден")
        
        # Запрос к диапазонной коллекции
        print("\nЗапрос к users_range:")
        count_range = client.testDB.users_range.count_documents({"age": {"$lte": 50}})
        print(f"- Документов с age <= 50: {count_range}")
        
    except OperationFailure as e:
        print(f"Ошибка запроса: {e.details['errmsg']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MongoDB Cluster Health Check')
    parser.add_argument('--host', default='localhost', help='MongoDB host')
    parser.add_argument('--mongos-port', type=int, default=27018, help='Mongos port')
    args = parser.parse_args()

    try:
        # Подключение к mongos
        client = MongoClient(f'mongodb://{args.host}:{args.mongos_port}')
        print("ПОДКЛЮЧЕНИЕ К КЛАСТЕРУ...")
        
        # Конфигурация сегментов
        shard_ports = {
            "shardReplSet1": [27022, 27023, 27024],
            "shardReplSet2": [27025, 27026, 27027]
        }

        # Выполнение проверок
        check_replication_status(shard_ports)
        check_cluster_status(client)
        print("\n--- РАСПРЕДЕЛЕНИЕ ДАННЫХ")
        check_data_distribution(client, "users_hash", shard_ports)
        check_data_distribution(client, "users_range", shard_ports)
        check_queries(client)
        
    except ConnectionFailure:
        print("Не удалось подключиться к кластеру MongoDB")
    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")