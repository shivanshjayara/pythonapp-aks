import uuid
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_instance_id():
    return f"This is my first aks deployment"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
