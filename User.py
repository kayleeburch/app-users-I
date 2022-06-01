from unicodedata import name


class User:

    def __init__(self, name, email, driver_licence, address, company = "Lyft"):
        self.name = name
        self.email = email
        self.driver_licence = driver_licence
        self.address = address
    def __str__(self):
        return f"I am {self.name}. My email is{self.email}, and my driver_licence is{self.driver_licence} and I live on {self.address}"

emily = User('Emily', 'emily@yahoo.com', '12342343343', '1234 lane road')
kaylee = User('Kaylee', 'kaylee@yahoo.com', '73743434223', '145 cypher road')
chris = User('Chris', 'chris@yahoo.com', '8394834334', '235 circle road')

print(emily)
print(kaylee)
print(chris)