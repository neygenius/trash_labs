import mysql.connector
from re import fullmatch

cnx = mysql.connector.connect(user="root", password='neygen', host='localhost', database='taxi_pool')

cursor = cnx.cursor(prepared=True)


# 1. Запрос: Вывести все автомобили, выпущенные в N-ом году, с указанием их модели
def get_all_cars_with_models_for_specified_year(year):
    query = """
    SELECT cars.car_id, cars.license_plate, cars.year, car_models.model_name, car_models.manufacturer 
    FROM cars
    JOIN car_models ON cars.model_id = car_models.model_id 
    WHERE cars.year = %s;
    """
    cursor.execute(query, (year,))
    for (car_id, license_plate, year, model_name, manufacturer) in cursor:
        print(f"Car ID: {car_id}, License plate: {license_plate}, Year: {year}, Model name: {model_name}, Manufacturer: {manufacturer}")


# 2. Запрос: Вывести информацию о количестве поездок, выполненных каждым водителем
def get_trips_count_for_each_driver():
    query = """
    SELECT drivers.first_name, drivers.last_name, COUNT(trips.trip_id) AS count 
    FROM drivers
    LEFT JOIN trips ON drivers.driver_id = trips.driver_id
    GROUP BY drivers.driver_id 
    ORDER BY count DESC;
    """
    cursor.execute(query)
    for (first_name, last_name, count) in cursor:
        print(f"First name: {first_name}, Last name: {last_name}, Trips count: {count}")


# 3. Запрос: Вывести информацию о статистике использования автомобилей водителями (водители могут совершать поездки на разных автомобилях)
def get_cars_stats_for_each_driver():
    query = """
    SELECT drivers.first_name, drivers.last_name, cars.license_plate, COUNT(trips.trip_id) AS count
    FROM drivers
    JOIN trips ON drivers.driver_id = trips.driver_id
    JOIN cars ON trips.car_id = cars.car_id
    GROUP BY drivers.driver_id, cars.car_id;
    """
    cursor.execute(query)
    for (first_name, last_name, license_plate, count) in cursor:
        print(f"First name: {first_name}, Last name: {last_name}, License plate: {license_plate}, Trips count: {count}")


# 4. Запрос: Вывести информацию о клиентах, которые совершили более трех поездок
def get_customers_with_three_more_trips():
    query = """
    SELECT customers.first_name, customers.last_name, COUNT(trips.trip_id) AS count
    FROM customers
    JOIN trips ON customers.customer_id = trips.customer_id
    GROUP BY customers.customer_id 
    HAVING COUNT(trips.trip_id) > 3;
    """
    cursor.execute(query)
    for (first_name, last_name, count) in cursor:
        print(f"First name: {first_name}, Last name: {last_name}, Trips count: {count}")


# 5. Запрос: Вывести список всех водителей, которые выполнили максимальное число поездок
def get_drivers_with_max_trips_count():
    query = """
    SELECT drivers.first_name, drivers.last_name 
    FROM drivers
    JOIN (
        SELECT driver_id, COUNT(trip_id) AS trip_count 
        FROM trips 
        GROUP BY driver_id) AS trip_counts ON drivers.driver_id = trip_counts.driver_id 
    WHERE trip_counts.trip_count = (
                                    SELECT MAX(trip_count) 
                                    FROM (
                                        SELECT COUNT(trip_id) AS trip_count 
                                        FROM trips 
                                        GROUP BY driver_id) AS max_count);
    """
    cursor.execute(query)
    for (first_name, last_name) in cursor:
        print(f"First name: {first_name}, Last name: {last_name}")


# 6. Запрос: Посчитать статистику длительности поездок (в минутах)
def get_trips_stats():
    query = """
    SELECT 
        MIN(TIMESTAMPDIFF(MINUTE, start_time, end_time)) AS min, 
        AVG(TIMESTAMPDIFF(MINUTE, start_time, end_time)) AS avg, 
        MAX(TIMESTAMPDIFF(MINUTE, start_time, end_time)) AS max 
    FROM trips;
    """
    cursor.execute(query)
    for (min, avg, max) in cursor:
        print(f"Min duration: {min}, Avg duration: {avg}, Max duration: {max}")


print("Запрос №2")
get_trips_count_for_each_driver()
print("Запрос №3")
get_cars_stats_for_each_driver()
print("Запрос №4")
get_customers_with_three_more_trips()
print("Запрос №5")
get_drivers_with_max_trips_count()
print("Запрос №6")
get_trips_stats()
print("Запрос №")

year = input("Введите год выпуска автомобиля: ")
print("Запрос №1")
get_all_cars_with_models_for_specified_year(year)

# Task 3
"""
insert = ("INSERT INTO customers(first_name, last_name, phone) VALUES(%s,%s,%s)")
first = 'Иван'
last = 'Иванов'
phone = '89276451344'

cursor.execute(insert, (first, last, phone))
cnx.commit()
print("\nКлиент добавлен!")
cursor.close()
cnx.close()
"""