from flask import Flask, render_template

from controllers.bookings_controller import bookings_blueprint
from controllers.services_controller import services_blueprint
from controllers.clients_controller import clients_blueprint
from controllers.photographers_controller import photographers_blueprint

app = Flask(__name__)

app.register_blueprint(photographers_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(services_blueprint)
app.register_blueprint(clients_blueprint)


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
