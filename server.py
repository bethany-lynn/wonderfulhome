from flask import Flask, render_template;
from jinja2 import StrictUndefined;
from model import *;
# import './static/css/main.css';

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """view homepage"""
    return render_template('index.html')

@app.route('/about')
def about_page():
    """Information about Jim and Angela and their business"""
    return render_template('about.html')

@app.route('/consultations')
def consultation_page():
    """Snippit about consultations"""
    return render_template('consultations.html')

@app.route('/services')
def services_page():
    """List of services and prices"""
    # offer a starting price, consult price, range of prices, 
    # and button to contact for more detailed pricing
    return render_template('services.html')

@app.route('/reviews')
def reviews_page():
    """Reviews and blurbs from previous clients"""
    return render_template('reviews.html')

@app.route('/gallery')
def gallery_page():
    """Images of previous work done"""
    return render_template('gallery.html')

@app.route('/contact')
def contact_page():
    """Phone number, email, Facebook page, Instagram page, YouTube channel"""
    return render_template('contact.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)