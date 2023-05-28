from faker import Faker, Generator, Factory

# Faker.seed(10)
fake = Faker("zh-CN")

print(fake.country_code())
print(fake.current_country())

