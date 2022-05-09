class User:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.addresses = []

  def add_address(self, new_address):
    self.addresses.append(new_address)

class Address:
  def __init__(self, street, city, state, zip_code):
    self.street = street
    self.city = city
    self.state = state
    self.zip_code = zip_code


roberto = User("Roberto", "Salazar")
first_street = Address("First Street", "Miami", "FL", 34189)
second_street = Address("Second Street", "Miami", "FL", 32154)
print(f"My name is {roberto.first_name} {roberto.last_name}")
roberto.add_address(first_street)
roberto.add_address(second_street)
print(roberto.addresses[0].street)