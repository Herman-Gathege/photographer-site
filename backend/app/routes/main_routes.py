from flask import Blueprint, render_template
from datetime import datetime


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', now=datetime.now())

@main_bp.route('/contact')
def contact():
    return render_template('contact.html', now=datetime.now())

@main_bp.route('/gallery')
def gallery():
    return render_template('gallery.html', now=datetime.now())

@main_bp.route('/blog')
def blog():
    return render_template('blog.html', now=datetime.now())