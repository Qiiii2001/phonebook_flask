# render_templae: A utility for rendering HTML templates
# Bluepoint: A tool for organizing and registering different routes, event handlers, etc., in the application
from flask import Blueprint, render_template

# Create a Bluepoint object called site
# split your application into distinct sections, each with its own routes and view functions. 
# In this example, it also specifies the template folder as site_templates, indicating that Flask should look for HTML template files in this folder.
site = Blueprint('site',__name__,template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')