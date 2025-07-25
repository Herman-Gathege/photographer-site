from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class BlogPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])

    # ✅ Updated: allow multiple files
    images = MultipleFileField("Upload Images", validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'Images only!')
    ])

    submit = SubmitField("Publish")

    # ✅ Updated: allow multiple files