from db.run_sql import run_sql
from models.client import Client


def save(client):
    sql = "INSERT INTO clients (name, client_from, email, birthdate, contact) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [client.name, client.client_from,
              client.email, client.birthdate, client.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id


def select(id):
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    client = Client(result["name"], result["client_from"], result["email"],
                    result["birthdate"], result["contact"], result["id"])
    return client


def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    for result in results:
        client = Client(result["name"], result["client_from"], result["email"],
                        result["birthdate"], result["contact"], result["id"])
        clients.append(client)
    return clients


def delete(id):
    sql = "DELETE FROM clients WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)


def update(client):
    sql = "UPDATE clients SET (name, client_from, email, birthdate, contact) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [client.name, client.client_from,
              client.email, client.birthdate, client.contact, client.id]
    run_sql(sql, values)
