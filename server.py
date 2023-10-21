from flask import Flask, render_template;
from jinja2 import StrictUndefined;
from model import *;

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
    return render_template('services.html')

# @app.route('/reviews')
# def reviews_page():
#     """Reviews and blurbs from previous clients"""
#     return render_template('reviews.html')

@app.route('/gallery')
def gallery_page():
    """Images of previous work done"""
    return render_template('gallery.html')

@app.route('/contact')
def contact_page():
    """Phone number, email, Facebook page, Instagram page, YouTube channel"""
    return render_template('contact.html')

"""All gallery routes below for each individual room"""

@app.route('/kitchens')
def kitchen_page():
    """Show gallery of kitchen images"""
    return render_template('kitchens.html')

@app.route('/bathrooms')
def bathroom_page():
    """Show gallery of bathroom images"""
    return render_template('bathrooms.html')

@app.route('/exteriors')
def exterior_page():
    """Show gallery of kitchen images"""
    return render_template('exteriors.html')

@app.route('/dining')
def dining_page():
    """Show gallery of dining, living, and entertainment images"""
    return render_template('dining.html')

@app.route('/bedrooms')
def bedroom_page():
    """Show gallery of bedroom images"""
    return render_template('bedrooms.html')

@app.route('/pantries')
def pantry_page():
    """Show gallery of pantry and custom organization images"""
    return render_template('pantries.html')

@app.route('/templates/<gallery_name>.html')
def get_gallery_template(gallery_name):
    """Show gallery of relevant button clicked """
    return render_template(f'{gallery_name}.html')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)