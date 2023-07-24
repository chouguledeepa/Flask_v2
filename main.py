from flask import Flask, render_template,abort,jsonify
from modals.dal import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("welcome.html", cards=db)


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html", card=card, index=index)
    except IndexError:
        abort(404)

@app.route("/api/cards")
def cards_list():
    #return jsonify(db)
    return db


if __name__ == '__main__':  # ,
    app.run(debug="True")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
