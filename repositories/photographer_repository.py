from db.run_sql import run_sql
from models.photographer import Photographer
from models.client import Client
from models.service import Service


def save(photographer):
    sql = "INSERT INTO photographers (name, email, portfolio_address) VALUES (%s, %s, %s) RETURNING id"
    values = [photographer.name,
              photographer.email, photographer.portfolio_address]
    results = run_sql(sql, values)
    id = results[0]['id']
    photographer.id = id


def select(id):
    sql = "SELECT * FROM photographers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    photographer = Photographer(
        result["name"], result["email"], result["portfolio_address"], result["id"])
    return photographer


def select_all():
    photographers = []
    sql = "SELECT * FROM photographers"
    results = run_sql(sql)
    for result in results:
        photographer = Photographer(
            result["name"], result["email"], result["portfolio_address"], result["id"])
        photographers.append(photographer)
    return photographers


def delete(id):
    sql = "DELETE FROM photographers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM photographers"
    run_sql(sql)


def update(photographer):
    sql = "UPDATE photographers SET (name, email, portfolio_address) = (%s, %s, %s) WHERE id = %s"
    values = [photographer.name,
              photographer.email, photographer.portfolio_address, photographer.id]
    run_sql(sql, values)


def select_clients_of_photographer(id):
    clients = []
    sql = "SELECT clients.* FROM clients INNER JOIN bookings ON bookings.client_id = clients.id WHERE bookings.photographer_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        client = Client(result["name"], result["client_from"], result["email"],
                        result["birthdate"], result["contact"])
        clients.append(client)
    return clients


def select_service_of_photographer(id):
    services = []
    sql = "SELECT services.* FROM services INNER JOIN bookings ON bookings.service_id = services.id WHERE bookings.photographer_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        service = Service(result["photo_type"],
                          result["hours"], result["price"])
        services.append(service)
    return services
