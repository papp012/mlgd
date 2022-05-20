from flask import Flask, render_template, url_for, jsonify
import math


app = Flask('codecool_series')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rolunk')
def about_page():
    return render_template('about-us.html')

@app.route('/blogs')

def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
