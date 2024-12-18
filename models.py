from sqlalchemy import Column, String, Integer, Double, TIMESTAMP, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class CarModel(Base):
  __tablename__ = 'car_models'
  
  model_id = Column(Integer, primary_key=True, autoincrement=True)
  model_name = Column(String(30))
  manufacturer = Column(String(30))

  def __init__(self, model_id, model_name, manufacturer):
    self.model_id = model_id
    self.model_name = model_name
    self.manufacturer = manufacturer


class Car(Base):
  __tablename__ = 'cars'
  
  car_id = Column(Integer, primary_key=True, autoincrement=True)
  license_plate = Column(String(9))
  model_id = Column(Integer, ForeignKey('car_models.model_id'))
  year = Column(Integer)
  notes = Column(JSON)

  model = relationship("CarModel", backref="cars")

  def __init__(self, car_id, license_plate, model_id, year, notes):
    self.car_id = car_id
    self.license_plate = license_plate
    self.model_id = model_id
    self.year = year
    self.notes = notes


class Customer(Base):
  __tablename__ = 'customers'
  
  customer_id = Column(Integer, primary_key=True, autoincrement=True)
  first_name = Column(String(30))
  last_name = Column(String(30))
  phone = Column(String(12))

  def __init__(self, customer_id, first_name, last_name, phone):
    self.customer_id = customer_id
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone


class Driver(Base):
  __tablename__ = 'drivers'
  
  driver_id = Column(Integer, primary_key=True, autoincrement=True)
  first_name = Column(String(30))
  last_name = Column(String(30))
  license_number = Column(String(10))

  def __init__(self, driver_id, first_name, last_name, license_number):
    self.driver_id = driver_id
    self.first_name = first_name
    self.last_name = last_name
    self.license_number = license_number



class Trip(Base):
  __tablename__ = 'trips'
  
  trip_id = Column(Integer, primary_key=True, autoincrement=True)
  driver_id = Column(Integer, ForeignKey('drivers.driver_id'))
  car_id = Column(Integer, ForeignKey('cars.car_id'))
  customer_id = Column(Integer, ForeignKey('customers.customer_id'))
  start_lat = Column(Double)
  start_lon = Column(Double)
  end_lat = Column(Double)
  end_lon = Column(Double)
  start_time = Column(TIMESTAMP)
  end_time = Column(TIMESTAMP)
  cost = Column(Double)

  driver = relationship("Driver", backref="trips")
  car = relationship("Car", backref="trips")
  customer = relationship("Customer", backref="trips")

  def __init__(self, trip_id, driver_id, car_id, customer_id, start_lat, start_lon, end_lat, end_lon, start_time, end_time, cost):
    self.trip_id = trip_id
    self.driver_id = driver_id
    self.car_id = car_id
    self.customer_id = customer_id
    self.start_lat = start_lat
    self.start_lon = start_lon
    self.end_lat = end_lat
    self.end_lon = end_lon
    self.start_time = start_time
    self.end_time = end_time
    self.cost = cost