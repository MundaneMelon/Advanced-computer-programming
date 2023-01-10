class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = (self.street)
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return "\n".join(lines)

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.address = None

def main():
    manager = Employee(1, 'Leslie Smith')
    manager.address = Address("100 Cleveland Circle",
                              "SomeCity", "ST", "00000")

    print(manager.name)
    print(manager.address)


if __name__ == '__main__':
    main()