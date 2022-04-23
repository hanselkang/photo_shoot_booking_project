from db.run_sql import run_sql
from models.service import Service
import repositories.photographer_repository as photographer_repository


def save(service):
    sql = "INSERT INTO services(photo_type, hours, price) VALUES (%s, %s, %s) RETURNING id"
    values = [service.photo_type,
              service.hours, service.price]
    results = run_sql(sql, values)
    id = results[0]['id']
    service.id = id


def select(id):
    sql = "SELECT * FROM services WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    service = Service(result["photo_type"], result["hours"],
                      result["price"], result["id"])
    return service



def select_all():
    services = []
    sql = "SELECT * FROM services"
    results = run_sql(sql)
    for result in results:
        service = Service(result["photo_type"],
                          result["hours"], result["price"], result["id"])
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
    sql = "UPDATE services SET (photo_type, hours, price) = (%s, %s, %s) WHERE id = %s"
    values = [service.photo_type,
              service.hours, service.price, service.id]
    run_sql(sql, values)
