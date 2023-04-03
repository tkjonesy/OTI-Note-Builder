

class Vehicle:

    all_vehicles = []

    def __init__(self, color, year, make, model, tag):
        self.all_vehicles.append(self)
        self.color = color
        self.year = year
        self.make = make
        self.model = model
        self.tag = tag
        self.vehicle_introduced = False

    def get_label(self):
        return f'{self.color}, {self.year} {self.make} {self.model} tag # {self.tag}'

    def introduce_vehicle(self):
        if not self.vehicle_introduced:
            self.vehicle_introduced = True


class House:

    all_houses = []

    def __init__(self, address, city):
        self.all_houses.append(self)
        self.address = address
        self.city = city
        self.house_introduced = False
        self.subject_house = False

    def get_label(self):
        return f'{self.address} in {self.city}'

    def introduce_house(self):
        if not self.house_introduced:
            self.house_introduced = True

    def subjects_house(self):
        if not self.subject_house:
            self.subject_house = True


class Restaurant:

    all_restaurants = []
    restaurant_introduced = False

    def __init__(self, name, address, city, is_chain):
        self.all_restaurants.append(self)
        self.name = name
        self.address = address
        self.city = city
        self.chain = is_chain

    def get_label(self):
        if self.chain:
            return f'a "{self.name}" located at {self.address} in {self.city}'
        else:
            return f'"{self.name}" located at {self.address} in {self.city}'

    def introduce_restaurant(self):
        if not self.restaurant_introduced:
            self.restaurant_introduced = True


class Store:

    all_stores = []
    store_introduced = False

    def __init__(self, name, address, city, is_chain):
        self.all_stores.append(self)
        self.name = name
        self.address = address
        self.city = city
        self.chain = is_chain

    def get_label(self):
        if self.chain:
            return f'a "{self.name}" located at {self.address} in {self.city}'
        else:
            return f'"{self.name}" located at {self.address} in {self.city}'

    def introduce_store(self):
        if not self.store_introduced:
            self.store_introduced = True


class Building:

    all_buildings = []
    building_introduced = False

    def __init__(self, name, address, city):
        self.all_buildings.append(self)
        self.name = name
        self.address = address
        self.city = city

    def get_label(self):
        return f'"{self.name}" located at {self.address} in {self.city}'

    def introduce_store(self):
        if not self.building_introduced:
            self.building_introduced = True

# Un-Comment for example locations and vehicles
# House('2040 Tropic Bay Court', 'Orlando')
# House('1308 Meadow Finch Drive', 'Winter Garden')
#
# Vehicle('gray', '2009', 'Infiniti', 'G-37', 'RNJ965')
# Vehicle('blue', '2020', 'Toyota', 'RAV4', 'H67DNR')
