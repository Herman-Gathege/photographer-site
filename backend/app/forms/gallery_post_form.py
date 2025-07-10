# app/forms/gallery_post_form.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired

class GalleryPostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    image = FileField("Image", validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'Images only!')
    ])
    submit = SubmitField("Publish")
