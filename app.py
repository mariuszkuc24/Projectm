from flask import Flask, render_template
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
from AzureDB import AzureDB
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/result')
def result():
    with AzureDB() as a:
        data = a.azureGetData()
    return render_template("result.html", data = data)
@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/error_denied')
def error_denied():
    abort(401)
@app.route('/error_internal')
def error_internal():
    return render_template('template.html', name='ERROR 505'), 505
@app.route('/error_not_found')
def error_not_found():
    response = make_response(render_template('template.html', name='ERROR 404'), 404)
    response.headers['X-Something'] = 'A value'
    return response
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0")