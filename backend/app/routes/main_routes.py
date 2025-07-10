from flask import Blueprint, render_template
from datetime import datetime
from app.models import BlogPost



main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', now=datetime.now())

@main_bp.route('/contact')
def contact():
    return render_template('contact.html', now=datetime.now())

@main_bp.route('/gallery')
def gallery():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    # Assign shape classes in a pattern
    shape_classes = ['wide', '', 'tall', '', '', 'wide']  # Customize pattern as needed

    for i, post in enumerate(posts):
        post.image_class = shape_classes[i % len(shape_classes)]
        
    return render_template('gallery.html', now=datetime.now(), posts=posts)

# @main_bp.route('/blog')
# def blog():
#     return render_template('blog.html', now=datetime.now())