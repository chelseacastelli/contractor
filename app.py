from flask import Flask, render_template

app = Flask(__name__)

# OUR MOCK ARRAY OF PROJECTS
vinyls = [
    { 'artist': 'Fleetwood Mac', 'album': 'Rumours', 'price': 24.98, 'image': './static/fleetwood_mac.jpeg' },
    { 'artist': 'Hozier', 'album': 'Wasteland, Baby!', 'price': 25.66, 'image': './static/hozier.jpg' }
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