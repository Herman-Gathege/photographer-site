from flask import Blueprint

booking_bp = Blueprint('booking', __name__, url_prefix='/booking')

# Add a simple route to satisfy the import for now
@booking_bp.route('/')
def blog_home():
    return "booking Home (placeholder)"
