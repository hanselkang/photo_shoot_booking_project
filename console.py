import pdb

from console_dummy.bookings import *
from console_dummy.clients import *
from console_dummy.confirmation import *
from console_dummy.photographers import *
from console_dummy.services import *



import repositories.client_repository as client_repository
import repositories.photographer_repository as photographer_repository
import repositories.service_repository as service_repository
import repositories.booking_repository as booking_repository
import repositories.booking_confirmation_repository as booking_confirmation_repostiory


booking_repository.delete_all()
booking_confirmation_repostiory.delete_all()
service_repository.delete_all()
photographer_repository.delete_all()
client_repository.delete_all()


for client in clients:
    client_repository.save(client)


for photographer in photographers:
    photographer_repository.save(photographer)
    

for service in services:
    service_repository.save(service)

for booking in bookings:
    booking_repository.save(booking)

for booking_confirmation in booking_confirmations:
    booking_confirmation_repostiory.save(booking_confirmation)
    
# print(photographer_repository.select_client_of_photographer(1))


# client_repository.delete(2)
# print(client_repository.select(1))
# print(booking_repository.select(1))
# print(photographer_repository.select(1))
# print(service_repository.select(1))
# print(booking_repository.select_all())
# print(photographer_repository.select_all())
# print(service_repository.select_all())
