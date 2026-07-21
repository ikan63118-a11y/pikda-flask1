from flask import Flask, render_template, request, redirect, url_for, flash
import os


app = Flask(__name__)

app.secret_key = "pikda-secret-key"


# =========================
# DATA PRODUK
# =========================

products = [

    {
        "id": 1,
        "nama": "PIKDA Original",
        "harga": 15000,
        "berat": "100 gram",
        "stok": 50,
        "gambar": "hero.png",
        "deskripsi": "Keripik singkong premium dengan rasa lada khas PIKDA yang gurih, renyah, dan pedas alami."
    },

    {
        "id": 2,
        "nama": "PIKDA Pedas Level 2",
        "harga": 17000,
        "berat": "100 gram",
        "stok": 40,
        "gambar": "hero.png",
        "deskripsi": "Sensasi pedas lada pilihan dengan cita rasa kuat yang bikin nagih."
    },

    {
        "id": 3,
        "nama": "PIKDA Extra Pedas",
        "harga": 20000,
        "berat": "100 gram",
        "stok": 30,
        "gambar": "hero.png",
        "deskripsi": "Varian khusus bagi pecinta pedas dengan bumbu lada lebih berani."
    }

]


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return render_template(
        "home.html",
        products=products
    )



# =========================
# PRODUCTS
# =========================

@app.route("/products")
def products_page():

    return render_template(
        "products.html",
        products=products
    )



# =========================
# DETAIL PRODUK
# =========================

@app.route("/product/<int:id>")
def product_detail(id):

    product = None

    for item in products:

        if item["id"] == id:
            product = item
            break


    if product is None:

        return render_template("404.html"), 404


    return render_template(
        "product_detail.html",
        product=product
    )



# =========================
# CHECKOUT
# =========================

@app.route("/checkout/<int:id>", methods=["GET","POST"])
def checkout(id):

    product = None


    for item in products:

        if item["id"] == id:
            product = item
            break



    if product is None:

        return render_template("404.html"), 404



    if request.method == "POST":

        nama = request.form["nama"]

        flash(
            f"Pesanan berhasil dibuat. Terima kasih {nama}!",
            "success"
        )

        return redirect(
            url_for("home")
        )



    return render_template(
        "checkout.html",
        product=product
    )



# =========================
# ERROR 404
# =========================

@app.errorhandler(404)
def not_found(error):

    return render_template(
        "404.html"
    ),404



# =========================
# RUN
# =========================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )


    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
