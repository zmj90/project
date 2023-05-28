from faker import Faker
fake = Faker()
Faker.seed(4321)

print(fake.name())
# 'Margaret Boehm'

