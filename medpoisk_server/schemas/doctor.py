from pydantic import BaseModel
from uuid import uuid4, UUID
from faker import Faker


class DoctorBase(BaseModel):
    name: str

class Doctor(DoctorBase):
    id: UUID

class DoctorPublick(DoctorBase):
    pass


# fake = Faker()
# Faker.seed(0)

# fake_doctors_db = [
#     Doctor(
#         id=uuid4(),
#         name=fake.name(),
#     )
#     for n in range(3)
# ]