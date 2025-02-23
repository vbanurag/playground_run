from abc import abstractmethod, ABC, ABCMeta

class AccountStatus(enum.Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    BLOCKED = 5

class AccountType(enum.Enum):
    ADMIN = 1
    Customer = 2
    SYSTEM = 3

class BikeType(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class ScooterType(enum.Enum):
    GAS = 1
    ELECTRIC = 2

class ReservationStatus(enum.Enum):
    ACTIVE = 1
    PENDING = 2
    CONFIRMED = 3
    COMPLETED = 4
    CANCELED = 5

class Person:
    def __init__(self,name, address, email, ph):
        self.name = name
        self.address = address
        self.email = email
        self.ph = ph

class Address:
    def __init__(self, street, city, state,zip, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country


class Account(Person, metaclass=ABCMeta):
    def __init__(self, name, address, email, ph, password):
        super().__init__(name, address, email, ph)
        self.__account_id = account_id
        self.__password = password
        self.__status = AccountStatus.NONE


    @abstractmethod
    def reset_password(self):
        pass


class SystemAdmin(Account):
    def __init__(self, name, address, email, ph, password):
        super().__init__(name, address, email, ph, password)
        self.__date_joined = Date.now()
        self.__account_type = AccountType.SYSTEM
    
    def search_customer(self, name):
        pass

    def add_reservation(self):
        None

    def cancel_reservation(self):
        None

    def reset_password(self):
        # functionality
        pass

class SystemAdmin(Account):
    def __init__(self, name, address, email, ph, password, licence_no, licence_expiry):
        super().__init__(name, address, email, ph, password)
        self.__date_joined = Date.now()
        self.__licence_no = licence_no
        self.__licence_expiry = licence_expiry
    
    def add_reservations(self):
        pass

    def get_reservations(self):
        None

    def cancel_reservation(self):
        None

    def reset_password(self):
        # functionality
        pass



class Vehicle(ABC):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log):
        self.__vehicle_id = vehicle_id
        self.__vehicle_idn_no = vehicle_idn_no
        self.__status = status
        self.__model = model
        self.__manf_yr = manf_yr
        self.__vehicle_log = vehicle_log

    def reserve_vehicle(self, vehicle_id):
        None

    def return_vehicle(self, vehicle_id):
        None

class Bike(Vehicle, metaclass=ABCMeta):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log)

class Scooter(Vehicle, metaclass=ABCMeta):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log, registration_no):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log)
        self.__reg_plate_no = registration_no

class SmallBike(Bike):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log)
        self.__type = BikeType.SMALL


class MediumBike(Bike):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log)
        self.__type = BikeType.MEDIUM

class LargeBike(Bike):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log)
        self.__type = BikeType.LARGE

class GasScooter(Scooter):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log, registration_no):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log, registration_no)
        self.__type = ScooterType.GAS

class ElectricScooter(Scooter):
    def __init__(self, vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log, registration_no):
        super().__init__(vehicle_id, vehicle_idn_no, status, model, manf_yr, vehicle_log, registration_no)
        self.__type = ScooterType.ELECTRIC

class Service(ABC):
    def __init__(self, service_id, price):
        self.__service_id = service_id
        self.__price = price

class RoasSideAssistance(Service):
    def __init__(self, service_id, price):
        super().__init__(service_id, price)


class Notification(ABC):
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content
    
    @abstractmethod
    def send_notification(self, account_id):
        pass

class SMSNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)  

    
    def send_notification(self, account_id):
        None


class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content):
        super().__init__(notification_id, created_on, content)

    def send_notification(self, account_id):
        None

class ParkingStall:
    def __init__(self, stall_id, stall_name, location):
        self.__stall_id = stall_id
        self.__stall_name = stall_name
        self.__location = location

class VehicleLog:
    def __init__(self, log_id, type, desc, created_on):
        self.__log_id = log_id
        self.__type = type
        self.__desc = desc
        self.__created_on = created_on

class VehicleReservation:
    def __init__(self, reservation_id, vehicle_id, start_date, end_date, pick_up_location, return_location, status):
        self.__reservation_id = reservation_id
        self.__vehicle_id = vehicle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__pick_up_location = pick_up_location
        self.__return_location = return_location
        self.__status = status
    
        self.__services = []

    
    def add_services(self, services):
        pass


class Search(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def search_by_type(self, type):
        pass

    def search_by_model(self, model):
        pass

class VehicleCatalog(Search):
    def __init__(self):
        self.vehicle_type = {}  # mapping of vehcile types
        self.vehicle_model = {}  # mapping of vehicle models

    def search_by_type(self, type):
        pass
    
    def search_by_model(self, model):
        pass


class RentalBranch:
    def __init__(self, branch_id, branch_name, stalls, location):
        self.__branch_id = branch_id
        self.__branch_name = branch_name
        self.__stalls = stalls
        self.__location = location
    


class __RentalSystem(object):
    __instances = None

    def __init__(cls):
        if cls.__instances is None:
            cls.__instances = super(__RentalSystem, cls).__new__(cls)
        return cls.__instances


class RentalSystem(metaclass=__RentalSystem):
    
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__rental_branches = []
        self.__vehicle_catalog = VehicleCatalog()
        self.__notifications = []
        self.__accounts = []
        self.__reservations = []
        self.__vehicles = []
        self.__services = []
        self.__notifications = []
        self.__accounts = []
        self.__reservations = []
        self.__vehicles = []
        self.__services = []
        self.__notifications = []
        self.__accounts = []
        self.__reservations = []
        self.__vehicles = []
        self.__services = []
        self.__notifications = []
        self.__accounts = []
        self.__reservations = []
        self.__vehicles = []
        self.__services = []
        self.__notifications = []
        self.__accounts = []
        self.__reservations = []
        self.__vehicles = []
        self.__services = []
        self.__notifications = []
        self.__accounts = []
        



'''

# GET /api/bikes - Retrieves a list of available bikes.
# GET /api/scooters - Retrieves a list of available scooters.
# POST /api/rentals - Creates a new rental order.
# GET /api/rentals/{customerId} - Retrieves the rental history of a specific customer.
# PUT /api/rentals/{rentalId}/return - Marks a rental item (bike or scooter) as returned.
# GET /api/search?type=bike&size=medium&availability=available


'''