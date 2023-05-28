from faker import Faker

Faker.seed(20)

fake = Faker()
for _ in range(3):
    n1 = fake.random_digit()
    print(n1)

for _ in range(3):
    r1 = fake.bothify(text='Product Number: ?-##', letters='ABCDE')
    print(r1)
