from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
# from app.forms.blog_post_form import BlogPostForm
from app.forms.gallery_post_form import GalleryPostForm

from app.forms.change_credentials_form import ChangeCredentialsForm
from flask import get_flashed_messages
from app.models import BlogPost, Booking, User, db
from slugify import slugify
from werkzeug.security import generate_password_hash
from sqlalchemy import or_, func
from app.utils.cloudinary_helpers import upload_image  # 👈 import helper
from werkzeug.utils import secure_filename 


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
def dashboard():
    
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    blog_posts = BlogPost.query.filter_by(post_type='blog').order_by(BlogPost.created_at.desc()).all()

    return render_template("admin/dashboard.html", user=current_user, posts=posts, blog_posts=blog_posts)

@admin_bp.route('/blog/new', methods=['GET', 'POST'])
@login_required
def create_post():
    form = GalleryPostForm()
    if form.validate_on_submit():
        slug = slugify(form.title.data)
        image_url = None

        if form.image.data:
            image_file = form.image.data
            image_url = upload_image(image_file)

        post = BlogPost(
            title=form.title.data,
            content=form.content.data,
            image_url=image_url,
            slug=slug 
        )
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "success")
        return redirect(url_for('admin.dashboard'))

    return render_template("admin/create_post.html", form=form)

@admin_bp.route('/blog/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = BlogPostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data

        # Check if new image file uploaded
        if form.image.data:
            file = form.image.data
            post.image_url = upload_image(file)
        else:
            # Use manually entered image URL if provided
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

# View all bookings
@admin_bp.route('/bookings')
@login_required
def view_bookings():
    status = request.args.get('status')
    search = request.args.get('search')

    query = Booking.query

    if status:
        query = query.filter(Booking.status == status)

    if search:
        search_term = f"%{search.lower()}%"
        query = query.filter(
            or_(
                func.lower(Booking.name).like(search_term),
                func.lower(Booking.email).like(search_term),
                func.lower(Booking.session_type).like(search_term),
                func.lower(Booking.date_requested).like(search_term)
            )
        )

    bookings = query.order_by(Booking.created_at.desc()).all()
    return render_template('admin/bookings.html', bookings=bookings)

# Update status
@admin_bp.route('/bookings/<int:booking_id>/status/<string:new_status>', methods=['POST'])
@login_required
def update_booking_status(booking_id, new_status):
    booking = Booking.query.get_or_404(booking_id)
    booking.status = new_status
    db.session.commit()
    flash('Booking status updated.', 'success')
    return redirect(url_for('admin.view_bookings'))

# Delete booking
@admin_bp.route('/bookings/<int:booking_id>/delete', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    db.session.delete(booking)
    db.session.commit()
    flash('Booking deleted.', 'info')
    return redirect(url_for('admin.view_bookings'))


@admin_bp.route('/update-credentials', methods=['GET', 'POST'])
@login_required
def update_credentials():
    form = ChangeCredentialsForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.password = generate_password_hash(form.password.data)
        db.session.commit()
        flash("Credentials updated successfully!", "success")
        return redirect(url_for('admin.dashboard'))
    return render_template("admin/change_credentials.html", form=form)