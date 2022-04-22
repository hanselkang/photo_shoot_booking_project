import pdb


from models.client import Client
from models.service import Service
from models.photographer import Photographer
from models.booking import Booking


import repositories.client_repository as client_repository
import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
photographer_repository.delete_all()
service_repository.delete_all()
client_repository.delete_all()



client_1 = Client("George", "New Zealand", "George.g@gmail.g", 35, "092991")
client_repository.save(client_1)

client_2 = Client("June", "Canada", "June.j@jmail.j", 23, "092399")
client_repository.save(client_2)

photographer_1 = Photographer("Hansel", "webmaster@hanseul.com", "http://instagram.com/hansel_in_scotland")
photographer_repository.save(photographer_1)

service_1 = Service("Portrait", 2, "Royal Mile", 160, photographer_1.id)
service_repository.save(service_1)

service_2 = Service("Interior", 1, "Currie", 100, photographer_1.id)
service_repository.save(service_2)


booking_1 = Booking("Properties in Currie",1,"Currie",client_1.id,service_2.id,photographer_1.id )
booking_repository.save(booking_1)



print(client_repository.select(1))
print(booking_repository.select(1))
print(photographer_repository.select(1))
print(service_repository.select(1))

print(client_repository.select_all())
print(booking_repository.select_all())
print(photographer_repository.select_all())
print(service_repository.select_all())
