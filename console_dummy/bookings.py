from console_dummy.clients import *
from console_dummy.services import *
from console_dummy.photographers import *
from models.booking import Booking

booking_1 = Booking("Properties in Currie", "CircusLane DeanVillage", 1,
                    '2022-05-22 10:00:00', '2022-05-22 12:00', client_1, service_2, photographer_1)

booking_2 = Booking("Couple Travel Portrait", "OldTown NewTown, NewTown", 2,
                    '2022-05-30 14:00:00', '2022-05-30 16:00', client_2, service_1, photographer_2)

booking_3 = Booking("Holiday Outdoor Portrait", "HolyroodPark Grassmarket OldTown", 3,
                    '2022-06-07 16:00:00', '2022-06-07 18:00', client_3, service_5, photographer_1)

booking_4 = Booking("Graduation with family", "DeanVillage CaltonHill OldTown Grassmarket", 4,
                    '2022-06-08 10:00:00', '2022-06-08 12:00', client_4, service_5, photographer_3)

booking_5 = Booking("Buddy's Birthday Party", "HolyroodPark", 5,
                    '2022-05-22 10:00:00', '2022-05-22 13:00', client_5, service_4, photographer_1)

booking_6 = Booking("Short Portrait in Edinburgh", "OldTown NewTown", 2,
                    '2022-05-30 14:00:00', '2022-05-30 16:00', client_6, service_6, photographer_2)

booking_7 = Booking("Wedding in OldTown", "Grassmarket OldTown", 20,
                    '2022-06-07 16:00:00', '2022-06-07 18:00', client_7, service_2, photographer_3)

booking_8 = Booking("Properties selling", "DeanVillage", 3,
                    '2022-06-08 10:00:00', '2022-06-08 12:00', client_8, service_3, photographer_1)

bookings = [booking_1,booking_2,booking_3,booking_4, booking_5, booking_6,booking_7,booking_8]