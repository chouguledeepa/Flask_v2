from flask import Flask, render_template,abort
from modals.dal import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/card/<int:index>")
def card_vew(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index)
    except IndexError:
        abort(404)


if __name__ == '__main__':  # ,
    app.run(debug="True")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
