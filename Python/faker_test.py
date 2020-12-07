from faker import Faker
from faker.providers import internet
from faker.providers import automotive

fake = Faker()

x = fake.name()
print(x)

y = fake.address()
print(y)

z = fake.text()
print(z)

fake.add_provider(internet)

print(fake.ipv4_private())

for _ in range(10):
  q = (fake.name())
  print(q)


fake.add_provider(automotive)
c = fake.license_plate()
print(c)