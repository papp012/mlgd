from flask import Flask, render_template, url_for, jsonify, request, redirect
from data import data_manager

app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def display_register_form():
    return render_template('register.html')


@app.route('/api/save-login', methods=['POST'])
def save_login_info():
    login_name = request.get_json()['loginName']
    login_email = request.get_json()['loginEmail']
    login_password = request.get_json()['loginPassword1']
    data_manager.save_user_to_database(login_name, login_email, login_password)
    return redirect('/')


@app.route('/login')
def display_login_form():
    return render_template('login.html')


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
