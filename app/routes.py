from flask import Flask, render_template

from app import app

@app.route("/")
@app.route("/<name>")
def hello(name = "World"):
    return render_template("index.html")

@app.route("/extract")
def extract():
    return render_template("extract.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/products/<product_id>")
def produkt(product_id):
    return render_template("product.html",product_id = product_id)

@app.route("/charts/<product_id>")
def charts(product_id):
    return render_template("charts.html",product_id = product_id)

@app.route("/author")
def author():
    return render_template("author.html")


