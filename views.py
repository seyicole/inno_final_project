from flask import Flask, render_template, Blueprint, redirect, url_for

my_view = Blueprint('my_view', __name__)


@my_view.route('/')
def index():
    return render_template('index.html')


@my_view.route('/about')
def about():
    return render_template('about.html')

@my_view.route('/contact')
def contact():
    return render_template('contact.html')

@my_view.route('/blog')
def blog():
    return render_template('blog.html')

@my_view.route('/faq')
def faq():
    return render_template('faq.html')

# @app.route('/page5')
# def page5():
#     return render_template('page5.html')

@my_view.route('/admin')
def admin():
    return render_template('admin.html')

