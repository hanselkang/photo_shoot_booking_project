from flask import Flask, render_template

from controllers.clients_controller import clients_blueprint

app = Flask(__name__)

app.register_blueprint(clients_blueprint)



@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
