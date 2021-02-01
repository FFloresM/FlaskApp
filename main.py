from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from forms.forms import NameForm
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'afobklsgsheknfrljnengliejbvnlirsbgvirhgbdr'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.nombre.data
		form.nombre.data=''
	return render_template(
				'index.html',
				form=form,
				name=name
				)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


		


#errors handlers
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)