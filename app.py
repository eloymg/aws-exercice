from flask import *
from flask_session import *
import random
import string
import subprocess
import time
import os
import redis

app = Flask(__name__)
app.secret_key = "aswdasdvoii"
if os.environ.get("SESSION_ENVIROMENT"):
    if os.environ["SESSION_ENVIROMENT"] == "redis":
        print("redis")
        app.config["SESSION_TYPE"] = "redis"
        app.config["SESSION_REDIS"] = redis.from_url("redis://redis.internal.com:6379")
    else:
        print("filesystem")
        app.config["SESSION_TYPE"] = "filesystem"
else:
    print("filesystem")
    app.config["SESSION_TYPE"] = "filesystem"

sess = Session()
sess.init_app(app)


@app.route("/")
def home():
    print(session["response"])
    t = session["response"] = randomString()
    res = make_response(
        "<p>The session is set with value: <strong>{}</strong></p>".format(t)
    )
    return res


@app.route("/get")
def getVariable():
    token = request.args.get("token")
    reference = request.args.get("reference")
    if token == session["response"]:
        s = session["response"]
        subprocess.Popen(["python stillcpu.py {}".format(reference)], shell=True)
        return render_template("getsession.html", name=s)
    else:
        return make_response("<h4>Bad Token!</h4>")


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(stringLength))


def stillCPU():
    a = True
    t = time.time()
    while a:
        time.sleep(0.0001)
        if (time.time() - t) > 10:
            a = False


if __name__ == "__main__":
    app.run(Debug=True)
