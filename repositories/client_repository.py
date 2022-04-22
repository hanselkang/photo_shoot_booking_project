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
    client = Client(result["name"], result["client_from"],
                    result["email"], result["age"], result["contact"], result["id"])
    return client

def delete_all():
    sql = "DELETE FROM clients"
    run_sql(sql)
