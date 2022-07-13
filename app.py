from flask import Flask, render_template, redirect, url_for
from views import my_view

app = Flask(__name__)
app.register_blueprint(my_view)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# @app.route('/javascript')
# def red():
#     return redirect(url_for('script'))

# @app.route('/script')
# def script():
#     return render_template('index.html')

# @app.route('/js')
# def blue():
#     return redirect(url_for('jsfile'))

# @app.route('/jsfile')
# def jsfile():
#     return render_template('index.html')




if __name__=="__main__":
    app.run(debug=True, port=8000)
