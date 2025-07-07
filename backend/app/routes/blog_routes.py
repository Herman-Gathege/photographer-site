from flask import Blueprint

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')

# Add a simple route to satisfy the import for now
@blog_bp.route('/')
def blog_home():
    return "Blog Home (placeholder)"
