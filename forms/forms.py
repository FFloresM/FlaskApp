from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required

class NameForm(FlaskForm):
	"""formulario NameForm"""
	nombre = StringField('Nombre', validators=[Required()])
	submit = SubmitField('Enviar')

class NuevaPilaForm(FlaskForm):
	"""dropdown para seleccionar pila"""
	nombre = StringField("Nombre Pila (id)", validators=[Required()])
	predio = StringField("Predio", validators=[Required()])
	estado = StringField("Estado", validators=[Required()])
	submit = SubmitField('Guardar')