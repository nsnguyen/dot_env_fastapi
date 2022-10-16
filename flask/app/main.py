import os

from dotenv import load_dotenv

from flask import Flask

load_dotenv()

here = os.getenv('location')

cool_dude = os.getenv('cool_dude')

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello {here} from Flask"

@app.route("/cool_dude")
def cool():
    return {"Hello": cool_dude}

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8000)