from db.run_sql import run_sql
from models.booking import Booking
from models.client import Client
from models.service import Service
import repositories.client_repository as client_repository
import repositories.service_repository as service_repository


def save(booking):
    sql = "INSERT INTO bookings (name, address, num_of_group, photoshoot_start_time, photoshoot_end_time, client_id, service_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [booking.name,
              booking.address, booking.num_of_group, booking.photoshoot_start_time, booking.photoshoot_end_time, booking.client.id, booking.service.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id





def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    client = client_repository.select(result["client_id"])
    service = service_repository.select(result["service_id"])
    booking = Booking(result["name"], result["address"],
                      result["num_of_group"], result["photoshoot_start_time"], result["photoshoot_end_time"], client, service, result["id"])
    return booking




def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        client = client_repository.select(result["client_id"])
        service = service_repository.select(result["service_id"])
        booking = Booking(result["name"], result["address"], result["num_of_group"], result["photoshoot_start_time"],
                          result["photoshoot_end_time"], client, service, result["id"])
        bookings.append(booking)
    return bookings


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def update(booking):
    sql = "UPDATE bookings (name, address, num_of_group, photoshoot_start_time, photoshoot_end_time, client_id, service_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = [booking.name,
              booking.address, booking.num_of_group, booking.photoshoot_start_time, booking.photoshoot_end_time, booking.client.id, booking.service.id]
    run_sql(sql, values)
