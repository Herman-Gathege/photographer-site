from flask import Blueprint, request, redirect, url_for, flash
from app.models import Booking
from app import db

booking_bp = Blueprint('booking', __name__, url_prefix='/booking')

# POST handler for the contact form
@booking_bp.route('/submit', methods=['POST'])
def submit_booking():
    name = request.form['name']
    email = request.form['email']
    session_type = request.form['session_type']
    date_requested = request.form['date_requested']
    message = request.form.get('message', '')

    new_booking = Booking(
        name=name,
        email=email,
        session_type=session_type,
        date_requested=date_requested,
        message=message
    )
    db.session.add(new_booking)
    db.session.commit()

    flash("📸 Booking submitted successfully! We'll be in touch.", "success")
    return redirect(url_for('main.home'))
