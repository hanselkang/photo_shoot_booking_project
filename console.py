import pdb


from models.client import Client
from models.photographer import Photographer
from models.service import Service
from models.booking import Booking


import repositories.client_repository as client_repository
import repositories.photographer_repository as photographer_repository
import repositories.service_repository as service_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
service_repository.delete_all()
photographer_repository.delete_all()
client_repository.delete_all()


client_1 = Client("George", "New Zealand",
                  "George.g@gmail.g", "19800113", "092991")
client_repository.save(client_1)

client_2 = Client("June", "Canada", "June.j@jmail.j", "19880324", "092399")
client_repository.save(client_2)

client_3 = Client("Alice", "Birmingham",
                  "Alice.a@amail.a", "19920822", "073299")
client_repository.save(client_3)

client_4 = Client("Claire", "South Korea",
                  "Clare.c@cmail.c", "19771201", "072129")
client_repository.save(client_4)

photographer_1 = Photographer(
    "Hansel", "webmaster@hanseul.com", "http://instagram.com/hansel_in_scotland")
photographer_repository.save(photographer_1)

photographer_2 = Photographer(
    "Marrie", "marrie@hanseul.com", "http://instagram.com/")
photographer_repository.save(photographer_2)

service_1 = Service("Portrait", 2, 160)
service_repository.save(service_1)

service_2 = Service("Interior", 1, 100)
service_repository.save(service_2)

service_3 = Service("Portrait", 2, 160)
service_repository.save(service_3)


booking_1 = Booking("Properties in Currie", "CircusLane DeanVillage", 1,
                    '2021-08-22 10:00:00', '2021-08-22 12:00', client_1, service_2, photographer_1)
booking_repository.save(booking_1)

booking_2 = Booking("Graduation Ceremony", "OldTown NewTown", 2,
                    '2021-11-22 14:00:00', '2021-11-22 16:00', client_2, service_3, photographer_2)
booking_repository.save(booking_2)

booking_3 = Booking("Holiday Outdoor Portrait", "HolyroodPark Grassmarket OldTown", 2,
                    '2021-12-23 16:00:00', '2021-12-24 18:00', client_3, service_1, photographer_1)
booking_repository.save(booking_3)

booking_4 = Booking("Holiday Outdoor Portrait", "DeanVillage CaltonHill OldTown Grassmarket", 1,
                    '2021-12-23 16:00:00', '2021-12-24 18:00', client_4, service_1, photographer_1)
booking_repository.save(booking_4)


# print(photographer_repository.select_client_of_photographer(1))


# client_repository.delete(2)
# print(client_repository.select(1))
# print(booking_repository.select(1))
# print(photographer_repository.select(1))
# print(service_repository.select(1))
# print(booking_repository.select_all())
# print(photographer_repository.select_all())
# print(service_repository.select_all())
