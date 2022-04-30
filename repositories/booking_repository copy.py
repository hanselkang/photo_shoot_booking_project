from db.run_sql import run_sql
from models.booking import Booking
import repositories.client_repository as client_repository
import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository

def save(booking):
    sql = "INSERT INTO bookings (name, places, num_of_group, photoshoot_start_time, photoshoot_end_time, client_id, service_id, photographer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [booking.name,
              booking.places, booking.num_of_group, booking.photoshoot_start_time, booking.photoshoot_end_time, booking.client.id, booking.service.id, booking.photographer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    client = client_repository.select(result["client_id"])
    service = service_repository.select(result["service_id"])
    photographer = photographer_repository.select(result["photographer_id"])
    booking = Booking(result["name"], result["places"],
                      result["num_of_group"], result["photoshoot_start_time"], result["photoshoot_end_time"], client, service, photographer, result["id"])
    return booking


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        client = client_repository.select(result["client_id"])
        service = service_repository.select(result["service_id"])
        photographer = photographer_repository.select(
            result["photographer_id"])
        booking = Booking(result["name"], result["places"], result["num_of_group"], result["photoshoot_start_time"],
                          result["photoshoot_end_time"], client, service, photographer, result["id"])
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
    sql = "UPDATE bookings SET (name, places, num_of_group, photoshoot_start_time, photoshoot_end_time, client_id, service_id, photographer_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [booking.name,
              booking.places, booking.num_of_group, booking.photoshoot_start_time, booking.photoshoot_end_time, booking.client, booking.service, booking.photographer, booking.id]
    run_sql(sql, values)
