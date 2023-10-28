from sqlalchemy.orm import Session

from .. import models, schemas

from uuid import UUID
from faker import Faker

fake = Faker()
Faker.seed(0)

places = []

def init_places(db):
    global places
    places = [
        schemas.PlaceCreate(
            title=fake.word(),
        )
        for _ in range(5)
    ]
    for i,place in enumerate(places):
        db_place = models.Place(**place.model_dump())
        db.add(db_place)
        db.commit()
        db.refresh(db_place)
        # places[i] = schemas.Place.model_validate(db_place)
        places[i] = schemas.Place.model_validate(db_place)

produsts = []

def init_products(db):
    global products
    products = [
        schemas.ProductCreate(
            title=fake.sentence(),
            min_amount=fake.random_number(digits=2),
            barcode=fake.random_number(digits=10)
        )
        for _ in range(5)
    ]
    for i,product in enumerate(products):
        db_product = models.Product(**product.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        products[i] = schemas.Product.model_validate(db_product)


def init_positions(db):
    for position in [
        schemas.PositionCreate(
            product = products[i],
            amount = fake.random_number(digits=2),
            place = places[i],
        )
        for i in range(5)
    ]:
        db_position = models.Position(
            product_id = position.product.id,
            place_id = position.place.id,
            amount = position.amount
        )
        db.add(db_position)
        db.commit()

def init_doctors(db):
    for doctor in [
        schemas.DoctorCreate(
            name=fake.word(),
        )
        for i in range(5)
    ]:
        db_doctor = models.Doctor(
            name=doctor.name
        )
        db.add(db_doctor)
        db.commit()


def init_rooms(db):
    for room in [
        schemas.RoomCreate(
            number=fake.building_number(),
        )
        for i in range(5)
    ]:
        db_room = models.Room(
            number=room.number
        )
        db.add(db_room)
        db.commit()