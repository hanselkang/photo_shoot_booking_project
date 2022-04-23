from db.run_sql import run_sql
from models.service import Service
import repositories.photographer_repository as photographer_repository


def save(service):
    sql = "INSERT INTO services(photo_type, place, hours, price, photographer) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [service.photo_type, service.place,
              service.hours, service.price, service.photographer]
    results = run_sql(sql, values)
    id = results[0]['id']
    service.id = id


def select(id):
    sql = "SELECT * FROM services WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    photographer = photographer_repository.select(result["photographer"])
    service = Service(result["photo_type"], result["place"],
                      result["hours"], result["price"], photographer, result["id"])
    return service


def select_all():
    services = []
    sql = "SELECT * FROM services"
    results = run_sql(sql)
    for result in results:
        photographer = photographer_repository.select(
            result["photographer"])
        service = Service(result["photo_type"], result["place"],
                          result["hours"], result["price"], photographer, result["id"])
        services.append(service)
    return services


def delete(id):
    sql = "DELETE FROM services WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM services"
    run_sql(sql)


def update(service):
    sql = "UPDATE services(photo_type, place, hours, price, photographer) VALUES (%s, %s, %s, %s, %s)"
    values = [service.photo_type, service.place,
              service.hours, service.price, service.photographer]
    run_sql(sql, values)
