from sqlalchemy import create_engine, select, text, func
from sqlalchemy.orm import sessionmaker

from models import CarModel, Car, Customer, Driver, Trip

engine = create_engine('mysql+mysqlconnector://root:neygen@localhost/taxi_pool')
Session = sessionmaker(bind=engine)
session = Session()


#------------------------------------------------------------------------------------------------------------
print("\n1. Вывести все автомобили, выпущенные в N-ом году, с указанием их модели:\n")

year = input("Введите год выпуска автомобиля: ")

stmt = (
    select(
        Car.car_id,
        Car.license_plate,
        Car.year,
        CarModel.model_name,
        CarModel.manufacturer
    )
    .join(CarModel, Car.model_id == CarModel.model_id)
    .where(Car.year == year)
)

result = session.execute(stmt)
for row in result:
    print(f"Car ID: {row.car_id}, License plate: {row.license_plate}, Year: {row.year}, Model name: {row.model_name}, Manufacturer: {row.manufacturer}")
print("")

#------------------------------------------------------------------------------------------------------------
print("2. Вывести информацию о количестве поездок, выполненных каждым водителем:")

stmt = (
    select(
        Driver.first_name,
        Driver.last_name,
        func.count(Trip.trip_id).label('count')
    )
    .join(Trip, Driver.driver_id == Trip.driver_id, isouter=True)
    .group_by(Driver.driver_id)
    .order_by(func.count(Trip.trip_id).desc())
)

result = session.execute(stmt)
for row in result:
    print(f"First name: {row.first_name}, Last name: {row.last_name}, Trips count: {row.count}")
print("")

#------------------------------------------------------------------------------------------------------------
print("3. Вывести информацию о статистике использования автомобилей водителями (водители могут совершать поездки на разных автомобилях):")

stmt = (
    select(
        Driver.first_name,
        Driver.last_name,
        Car.license_plate,
        func.count(Trip.trip_id).label('count')
    )
    .join(Trip, Driver.driver_id == Trip.driver_id)
    .join(Car, Trip.car_id == Car.car_id)
    .group_by(Driver.driver_id, Car.car_id)
)

result = session.execute(stmt)
for row in result:
    print(f"First name: {row.first_name}, Last name: {row.last_name}, License plate: {row.license_plate}, Trips count: {row.count}")
print("")

#------------------------------------------------------------------------------------------------------------
print("4. Вывести информацию о клиентах, которые совершили более трех поездок:")

stmt = (
    select(
        Customer.first_name, 
        Customer.last_name,
        func.count(Trip.trip_id).label('count')
    )
    .join(Trip, Customer.customer_id == Trip.customer_id)
    .group_by(Customer.customer_id)
    .having(func.count(Trip.trip_id) > 3)
)

result = session.execute(stmt)
for row in result:
    print(f"First name: {row.first_name}, Last name: {row.last_name}, Trips count: {row.count}")
print("")

#------------------------------------------------------------------------------------------------------------
print("5. Вывести список всех водителей, которые выполнили максимальное число поездок:")

subquery = (
    session.query(Trip.driver_id, func.count(Trip.trip_id).label('trip_count'))
    .group_by(Trip.driver_id)
    .subquery()
)

max_trip_count_subquery = (
    session.query(func.max(subquery.c.trip_count)).subquery()
)

stmt = (
    select(
        Driver.first_name, 
        Driver.last_name
    )
    .join(subquery, Driver.driver_id == subquery.c.driver_id)
    .filter(subquery.c.trip_count == max_trip_count_subquery)
)

result = session.execute(stmt)
for row in result:
    print(f"First name: {row.first_name}, Last name: {row.last_name}")
print("")

#------------------------------------------------------------------------------------------------------------
print("\n6. Посчитать статистику длительности поездок (в минутах):")

stmt = select(
    func.min(func.timestampdiff(text('MINUTE'), Trip.start_time, Trip.end_time)).label('min'),
    func.avg(func.timestampdiff(text('MINUTE'), Trip.start_time, Trip.end_time)).label('avg'),
    func.max(func.timestampdiff(text('MINUTE'), Trip.start_time, Trip.end_time)).label('max')
).select_from(Trip)

result = session.execute(stmt)

for row in result:
    print(f"Min duration: {row.min}s, Avg duration: {row.avg}s, Max duration: {row.max}s")
print("")


session.close()