from db.run_sql import run_sql
from models.service import Service


def save(service):
    sql = "INSERT INTO services (photo_type, place, hours, price, photographer_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [service.photo_type, service.place, service.hours, service.price, service.photographer_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    service.id = id


def delete_all():
    sql = "DELETE FROM services"
    run_sql(sql)
