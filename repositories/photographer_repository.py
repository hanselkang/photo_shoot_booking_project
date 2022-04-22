from db.run_sql import run_sql
from models.photographer import photographer


def save(photographer):
    sql = "INSERT INTO photographers (name, email, portfolio_address) VALUES (%s, %s, %s) RETURNING id"
    values = [photographer.name, photographer.email, photographer.portfolio_address]
    results = run_sql(sql, values)
    id = results[0]['id']
    photographer.id = id
