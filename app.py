from flask import Flask, render_template, redirect, url_for
from views import my_view

app = Flask(__name__)
app.register_blueprint(my_view)

# abort(500)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.route('/recipes')
def recipes():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html')




if __name__=="__main__":
    app.run(debug=True, port=8000)
