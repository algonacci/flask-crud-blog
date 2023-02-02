from flask import Flask, render_template
from db import cursor, db

app = Flask(__name__)


@app.get("/")
def root():
    cursor.execute("SELECT * FROM posts")
    data = cursor.fetchall()
    print(data)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
