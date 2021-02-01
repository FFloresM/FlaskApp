from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
	"""formulario NameForm"""
	nombre = StringField('Nombre', validators=[Required()])
	submit = SubmitField('Enviar')