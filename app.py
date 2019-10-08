from flask import Flask, render_template
from pymongo import MongoClient

# client = MongoClient()
# db = client.Contractor
# vinyls = db.vinyls

app = Flask(__name__)

vinyls = [
    { 'artist': 'Fleetwood Mac', 'album': 'Rumours', 'price': 24.98, 'image': './static/fleetwood_mac.jpeg' },
    { 'artist': 'Hozier', 'album': 'Wasteland, Baby!', 'price': 25.98, 'image': './static/hozier.jpeg' },
    { 'artist': 'Mac Miller', 'album': 'Blue Slide Park', 'price': 28.98, 'image': './static/mac_miller.jpeg'},
    { 'artist': 'Kehlani', 'album': 'While We Wait', 'price': 22.98, 'image': './static/kehlani.jpeg' },
    { 'artist': 'Paramore', 'album': 'Riot!', 'price': 20.98, 'image': './static/paramore.jpeg' },
    { 'artist': 'Russ', 'album': 'ZOO', 'price': 18.00, 'image': './static/russ.jpeg' },
    { 'artist': 'The 1975', 'album': 'A Brief Inquiry Into Online Relationships', 'price': 38.98, 'image': './static/1975.jpeg' },
    { 'artist': 'Troye Sivan', 'album': 'Bloom', 'price': 19.98, 'image': './static/troye_sivan.jpeg' },
    { 'artist': 'The Beatles', 'album': 'Abbey Road Anniversary', 'price': 35.98, 'image': './static/beatles.jpeg' }
]
@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.html', vinyls=vinyls)

@app.route('/vinyls')
def store_index():
    """Show all vinyls."""
    return render_template('index.html', vinyls=vinyls)

if __name__ == '__main__':
    app.run(debug=True)




