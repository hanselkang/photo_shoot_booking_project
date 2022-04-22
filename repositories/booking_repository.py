from db.run_sql import run_sql
from models.booking import Booking


def save(booking):
    sql = "INSERT INTO bookings (name, address, num_of_group, client_id, service_id, photographer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [booking.name,
              booking.address, booking.num_of_group, booking.client_id, booking.service_id, booking.photographer_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)
