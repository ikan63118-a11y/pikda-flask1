from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "pikda123"

# ======================================
# DATA PRODUK
# ======================================

products = [

    {
        "id": 1,
        "nama": "PIKDA Original",
        "harga": 15000,
        "gambar": "hero.png",
        "berat": "100 Gram",
        "stok": 50,
        "deskripsi": "Keripik singkong premium dengan bumbu lada khas PIKDA."
    },

    {
        "id": 2,
        "nama": "PIKDA Extra Pedas",
        "harga": 18000,
        "gambar": "hero.png",
        "berat": "100 Gram",
        "stok": 35,
        "deskripsi": "Varian extra pedas untuk pecinta makanan pedas."
    },

    {
        "id": 3,
        "nama": "PIKDA Family Pack",
        "harga": 28000,
        "gambar": "hero.png",
        "berat": "250 Gram",
        "stok": 20,
        "deskripsi": "Kemasan besar cocok untuk keluarga."
    },

    {
        "id": 4,
        "nama": "PIKDA Balado",
        "harga": 16000,
        "gambar": "hero.png",
        "berat": "100 Gram",
        "stok": 40,
        "deskripsi": "Rasa balado gurih pedas."
    },

    {
        "id": 5,
        "nama": "PIKDA BBQ",
        "harga": 17000,
        "gambar": "hero.png",
        "berat": "100 Gram",
        "stok": 25,
        "deskripsi": "Rasa barbeque favorit semua kalangan."
    },

    {
        "id": 6,
        "nama": "PIKDA Mix Pack",
        "harga": 40000,
        "gambar": "hero.png",
        "berat": "300 Gram",
        "stok": 15,
        "deskripsi": "Paket isi berbagai varian rasa."
    }

]

# ======================================
# HOME
# ======================================

@app.route("/")
def home():

    return render_template(
        "home.html",
        products=products[:3]
    )

# ======================================
# SEMUA PRODUK
# ======================================

@app.route("/products")
def products_page():

    return render_template(
        "products.html",
        products=products
    )
# ======================================
# DETAIL PRODUK
# ======================================

@app.route("/product/<int:id>")
def product_detail(id):

    product = None

    for p in products:

        if p["id"] == id:

            product = p

            break

    if product is None:

        return "Produk tidak ditemukan", 404

    return render_template(
        "product_detail.html",
        product=product
    )


# ======================================
# CHECKOUT
# ======================================

@app.route("/checkout/<int:id>", methods=["GET", "POST"])
def checkout(id):

    product = None

    for p in products:

        if p["id"] == id:

            product = p

            break

    if product is None:

        return "Produk tidak ditemukan",404

    if request.method == "POST":

        nama = request.form.get("nama")
        email = request.form.get("email")
        hp = request.form.get("hp")
        alamat = request.form.get("alamat")
        jumlah = request.form.get("jumlah")
        pembayaran = request.form.get("pembayaran")

        if not nama or not email or not hp or not alamat:

            flash(
                "Semua data wajib diisi!",
                "danger"
            )

            return redirect(
                url_for(
                    "checkout",
                    id=id
                )
            )

        flash(
            "Pesanan berhasil dibuat!",
            "success"
        )

        return redirect("/")

    return render_template(
        "checkout.html",
        product=product
    )


# ======================================
# ERROR PAGE
# ======================================

@app.errorhandler(404)
def not_found(error):

    return render_template(
        "404.html"
    ),404


# ======================================
# RUN
# ======================================

if __name__ == "__main__":

    app.run(
        debug=True
    )