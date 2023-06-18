from flask import Flask, render_template, request, redirect, flash
from db import cursor, db

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'



@app.get("/")
def root():
    cursor.execute("SELECT * FROM posts")
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

@app.get("/edit_post/<int:id>")
def edit_post(id):
    cursor.execute("SELECT * FROM posts WHERE id = ('{}')".format(id))
    data = cursor.fetchall()
    return render_template("edit_post.html", data=data)

@app.post("/update_post/<int:id>")
def update_post(id):
    title = request.form["title"]
    author = request.form["author"]
    body = request.form["body"]
    cursor.execute("""
        UPDATE posts SET
        title = '{}',
        author = '{}',
        body = '{}'
        WHERE id = {}
        """.format(title, author, body, id))
    db.commit()
    flash("Post has been updated successfully!", "success")
    return redirect("/")


@app.post("/delete_post/<int:id>")
def delete_post(id):
    cursor.execute("DELETE from posts WHERE id = ('{}')".format(id))
    db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run()
