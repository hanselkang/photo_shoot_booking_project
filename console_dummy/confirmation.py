from console_dummy.clients import *
from console_dummy.services import *
from console_dummy.photographers import *
from models.booking_confirmation import BookingConfirmation

booking_confirmation_1 = BookingConfirmation("Properties selling", "DeanVillage", 3,
                                            '2022-06-08 10:00:00', '2022-06-08 12:00', client_8, service_3, photographer_1)

booking_confirmations = [booking_confirmation_1]