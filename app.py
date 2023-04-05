
from flask import Flask, render_template, request
from telegram_send import send_data


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/load', methods=['GET'])
async def load():
    if request.method == "GET":
        data = request.args.to_dict()
        await send_data(**data)
        return render_template("finish.html")


app.run(host='0.0.0.0')
