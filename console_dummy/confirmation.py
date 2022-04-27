from console_dummy.clients import *
from console_dummy.services import *
from console_dummy.photographers import *
from models.booking_confirmation import BookingConfirmation

booking_confirmation_1 = BookingConfirmation("Properties for June", "CircusLane DeanVillage", 1,
                                             '2022-05-22 10:00:00', '2022-05-22 12:00', client_1, service_2, photographer_1)

booking_confirmations = [booking_confirmation_1]
