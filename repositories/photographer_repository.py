from db.run_sql import run_sql
from models.photographer import Photographer


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
    photographer = Photographer(result["name"], result["email"],
                                result["portfolio_address"], result["id"])
    return photographer


def select_all():
    photographers = []
    sql = "SELECT * FROM photographers"
    results = run_sql(sql)
    for result in results:
        photographer = Photographer(result["name"], result["email"],
                                    result["portfolio_address"], result["id"])
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
    sql = "UPDATE photographers (name, email, portfolio_address) VALUES (%s, %s, %s)"
    values = [photographer.name,
              photographer.email, photographer.portfolio_address]
    run_sql(sql, values)
