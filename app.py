from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Contractor')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

vinyls = db.vinyls
vinyls.drop()
carts = db.carts
carts.drop()


# Images from UrbanOutfitters - https://www.urbanoutfitters.com/
db.vinyls.insert_many([
    { 'artist': 'Hozier', 'album': 'Wasteland, Baby!', 'price': 25.98, 'image': './static/hozier.jpeg' },
    { 'artist': 'Mac Miller', 'album': 'Blue Slide Park', 'price': 28.98, 'image': './static/mac_miller.jpeg'},
    { 'artist': 'Kehlani', 'album': 'While We Wait', 'price': 22.98, 'image': './static/kehlani.jpeg' },
    { 'artist': 'Paramore', 'album': 'Riot!', 'price': 20.98, 'image': './static/paramore.jpeg' },
    { 'artist': 'Fleetwood Mac', 'album': 'Rumours', 'price': 24.98, 'image': './static/fleetwood_mac.jpeg' },
    { 'artist': 'Russ', 'album': 'ZOO', 'price': 18.98, 'image': './static/russ.jpeg' },
    { 'artist': 'Cigarettes After Sex', 'album': 'Cry', 'price': 24.98, 'image': './static/cigarettes_after_sex.jpeg' },
    { 'artist': 'Troye Sivan', 'album': 'Bloom', 'price': 19.98, 'image': './static/troye_sivan.jpeg' },
    { 'artist': 'The Beatles', 'album': 'Abbey Road', 'price': 35.98, 'image': './static/beatles.jpeg' },
    { 'artist': 'Lizzo', 'album': 'Cuz I Love You', 'price': 21.98, 'image': './static/lizzo.jpeg' },
    { 'artist': 'Queen', 'album': 'Greatest Hits', 'price': 35.98, 'image': './static/queen.jpeg' },
    { 'artist': 'Billie Eilish', 'album': 'don\'t smile at me', 'price': 21.98, 'image': './static/billie_eilish.jpeg' },
])

app = Flask(__name__)

@app.route('/')
def index():
    """Display items"""
    return render_template('index.html', vinyls=vinyls.find())


@app.route('/vinyls/<vinyl_id>/add', methods=['POST'])
def add_to_cart(vinyl_id):
    """"""
    if carts.find_one({'_id': ObjectId(vinyl_id)}):
        carts.update_one(
            {'_id': ObjectId(vinyl_id)},
            {'$inc': {'quantity': int(1)}}
        )
    else:
        carts.insert_one(
            {**vinyls.find_one({'_id': ObjectId(vinyl_id)}), **{'quantity': 1}})

    return redirect(url_for('show_cart'))

@app.route('/cart')
def show_cart():
    """Show cart."""
    cart = carts.find()
    # This will display all products by looping through the database
    total_price = list(carts.find({}))
    total = 0
    for i in range(len(total_price)):
        total += total_price[i]["price"]*total_price[i]["quantity"]
        round(float(total), 2)

    return render_template('cart.html', carts=cart, total=total)


@app.route('/carts/<cart_id>/delete', methods=['POST'])
def remove_from_cart(cart_id):
    # This will delete a product by using an id as a parameter
    """Remove one product from cart"""
    cart_item  = carts.find_one({'_id': ObjectId(cart_id)})
    carts.update_one(
        {'_id': ObjectId(cart_id)},
        {'$inc': {'quantity': -int(1)}}
    )

    if cart_item['quantity']==1:
        carts.remove({'_id': ObjectId(cart_id)})

    return redirect(url_for('show_cart'))


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))




