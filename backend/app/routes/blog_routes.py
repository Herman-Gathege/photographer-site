from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app.models import BlogPost, BlogImage
from app.forms.blog_post_form import BlogPostForm
from app.utils.cloudinary_helpers import upload_image
from app import db
from flask import request
from slugify import slugify
from datetime import datetime

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

@blog_bp.route('/')
def blog_home():
    posts = BlogPost.query.filter_by(post_type='blog').order_by(BlogPost.created_at.desc()).all()
    def serialize_post(post):
        return {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at.strftime('%B %d, %Y'),
            "images": [{"image_url": img.image_url} for img in post.images]
        }

    serialized_posts = [serialize_post(post) for post in posts]

    return render_template('blog/blog.html', posts=posts, post_json=serialized_posts, now=datetime.now())

@blog_bp.route('/new', methods=['GET', 'POST'])
@login_required
def create_blog_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        slug = slugify(form.title.data)

        post = BlogPost(
            title=form.title.data,
            content=form.content.data,
            slug=slug,
            post_type='blog'
        )
        db.session.add(post)
        db.session.commit()

        if form.images.data:
            for image in form.images.data:
                if image:
                    url = upload_image(image)
                    db.session.add(BlogImage(image_url=url, post_id=post.id))

        db.session.commit()
        flash("Blog post created!", "success")
        return redirect(url_for('blog.blog_home'))

    return render_template('blog/create_post.html', form=form)

@blog_bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = BlogPostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()

        # Upload any new images
        if form.images.data:
            for image in form.images.data:
                if image:
                    url = upload_image(image)
                    db.session.add(BlogImage(image_url=url, post_id=post.id))

        db.session.commit()
        flash("Blog post updated!", "success")
        return redirect(url_for('blog.blog_home'))

    return render_template('blog/edit_post.html', form=form, post=post)

@blog_bp.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)

    # Deletes all related images because of the cascade="all, delete-orphan"
    db.session.delete(post)
    db.session.commit()

    flash("Blog post deleted!", "info")
    return redirect(url_for('blog.blog_home'))

@blog_bp.route('/image/delete/<int:image_id>/<int:post_id>', methods=['POST'])
@login_required
def delete_blog_image(image_id, post_id):
    image = BlogImage.query.get_or_404(image_id)
    db.session.delete(image)
    db.session.commit()
    flash("Image deleted from post.", "warning")
    return redirect(url_for('blog.edit_blog_post', post_id=post_id))
