from flask import Flask, render_template, request, redirect
from db import cursor, db

app = Flask(__name__)


@app.get("/")
def root():
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
    data = cursor.fetchall()
    return render_template("index.html", data=data)


@app.get("/post/<int:id>")
def get_post_by_id(id):
    cursor.execute("SELECT * FROM posts WHERE id = ('{}')".format(id))
    data = cursor.fetchall()
    return render_template("post.html", data=data)


@app.route("/add_post", methods=["GET", "POST"])
def add_post():
    if request.method == "GET":
        return render_template("add_post.html")
    else:
        title = request.form["title"]
        author = request.form["author"]
        body = request.form["body"]
        cursor.execute("""
        INSERT INTO `posts`
        (`title`, `author`, `body`)
        VALUES
        ('{}', '{}', '{}')
        """.format(title, author, body))
        db.commit()
        return redirect("/")


if __name__ == "__main__":
    app.run()
