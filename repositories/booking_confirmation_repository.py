from db.run_sql import run_sql
from models.booking_confirmation import BookingConfirmation

import repositories.client_repository as client_repository
import repositories.service_repository as service_repository
import repositories.photographer_repository as photographer_repository


def save(booking_confirmation):
    sql = "INSERT INTO booking_confirmations (name, places, num_of_group, photoshoot_start_time, photoshoot_end_time, client_id, service_id, photographer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [booking_confirmation.name,
              booking_confirmation.places, booking_confirmation.num_of_group, booking_confirmation.photoshoot_start_time, booking_confirmation.photoshoot_end_time, booking_confirmation.client.id, booking_confirmation.service.id, booking_confirmation.photographer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking_confirmation.id = id


def select(id):
    sql = "SELECT * FROM booking_confirmations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    client = client_repository.select(result["client_id"])
    service = service_repository.select(result["service_id"])
    photographer = photographer_repository.select(result["photographer_id"])
    booking_confirmation = BookingConfirmation(result["name"], result["places"],
                      result["num_of_group"], result["photoshoot_start_time"], result["photoshoot_end_time"], client, service, photographer, result["id"])
    return booking_confirmation


def select_all():
    booking_confirmations = []
    sql = "SELECT * FROM booking_confirmations"
    results = run_sql(sql)
    for result in results:
        client = client_repository.select(result["client_id"])
        service = service_repository.select(result["service_id"])
        photographer = photographer_repository.select(
            result["photographer_id"])
        booking_confirmation = BookingConfirmation(result["name"], result["places"], result["num_of_group"], result["photoshoot_start_time"],
                          result["photoshoot_end_time"], client, service, photographer, result["id"])
        booking_confirmations.append(booking_confirmation)
    return booking_confirmations


def delete(id):
    sql = "DELETE FROM booking_confirmations WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM booking_confirmations"
    run_sql(sql)


def update(booking_confirmation):
    sql = "UPDATE booking_confirmations SET (name, places, num_of_group, photoshoot_start_time, photoshoot_end_time, client_id, service_id, photographer_id) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [booking_confirmation.name,
              booking_confirmation.places, booking_confirmation.num_of_group, booking_confirmation.photoshoot_start_time, booking_confirmation.photoshoot_end_time, booking_confirmation.client, booking_confirmation.service, booking_confirmation.photographer, booking_confirmation.id]
    run_sql(sql, values)
