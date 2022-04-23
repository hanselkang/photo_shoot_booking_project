from db.run_sql import run_sql
from models.client import Client


def save(client):
    sql = "INSERT INTO clients (name, client_from, email, age, contact) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [client.name, client.client_from,
              client.email, client.age, client.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id


def select(id):
    sql = "SELECT * FROM clients WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    client = Client(result["name"], result["client_from"], result["email"],
                    result["age"], result["contact"])
    return client


def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    for result in results:
        client = Client(result["name"], result["client_from"], result["email"],
                        result["age"], result["contact"])
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
    sql = "UPDATE clients (name, client_from, email, age, contact) VALUES (%s, %s, %s, %s, %s)"
    values = [client.name, client.client_from,
              client.email, client.age, client.contact]
    run_sql(sql, values)
