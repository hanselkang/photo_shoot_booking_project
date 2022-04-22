from db.run_sql import run_sql
from models.booking import Booking
import repositories.client_repository as client_repository
import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository


def save(booking):
    sql = "INSERT INTO bookings (name, address, num_of_group, client_id, service_id, photographer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [booking.name,
              booking.address, booking.num_of_group, booking.client_id, booking.service_id, booking.photographer_id]
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
    booking = Booking(result["name"], result["address"],
                    result["num_of_group"], client, service, photographer, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
