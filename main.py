from flask import Flask, render_template, url_for, jsonify
import math


app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def display_login_form():
    return render_template('login.html')


@app.route('/api/save-login')
def save_login_info():
    return ""


@app.route('/rolunk')
def about_page():
    return render_template('about-us.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/new-blogpost')
def display_new_blogpost_form():
    return render_template('new-blogpost.html')


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
