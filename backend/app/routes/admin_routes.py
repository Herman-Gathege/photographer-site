from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms.blog_post_form import BlogPostForm
from flask import get_flashed_messages
from app.models import BlogPost, db
from slugify import slugify


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
def dashboard():
    
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template("admin/dashboard.html", user=current_user, posts=posts)

@admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        slug = slugify(form.title.data)


        post = BlogPost(
            title=form.title.data,
            content=form.content.data,
            image_url=form.image_url.data,
            slug=slug 
        )
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for('admin.dashboard'))
    return render_template("admin/create_post.html", form=form)

# Edit a blog post
@admin_bp.route('/blog/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = BlogPostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.image_url = form.image_url.data
        db.session.commit()
        flash("Post updated!", "success")
        return redirect(url_for('admin.dashboard'))

    return render_template("admin/edit_post.html", form=form, post=post)

# Delete a blog post
@admin_bp.route('/blog/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted!", "info")
    return redirect(url_for('admin.dashboard'))