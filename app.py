from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("inventario.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    return render_template("index.html", productos=productos)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        conn = get_db()
        conn.execute("INSERT INTO productos (nombre,categoria,precio,stock) VALUES (?,?,?,?)",
                     (nombre,categoria,precio,stock))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    conn = get_db()
    producto = conn.execute("SELECT * FROM productos WHERE id=?",(id,)).fetchone()
    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = request.form["precio"]
        stock = request.form["stock"]
        conn.execute("UPDATE productos SET nombre=?,categoria=?,precio=?,stock=? WHERE id=?",
                     (nombre,categoria,precio,stock,id))
        conn.commit()
        conn.close()
        return redirect("/")
    conn.close()
    return render_template("edit.html", producto=producto)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM productos WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
