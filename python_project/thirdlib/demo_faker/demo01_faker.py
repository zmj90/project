"""

"""
from faker import Faker, Generator
from faker.providers import internet

fake = Faker("zh-CN")
fake.name()
fake.address()
fake.text()
fake.add_provider(internet)
fake.ipv4_private()
print(fake.word())
