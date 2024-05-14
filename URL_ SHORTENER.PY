from flask import Flask, render_template, request, redirect
import secrets

app = Flask(__name__)
urls = {}  # Dictionary to store original URLs

@app.route('/')
def index():
    return """
    <h1>URL Shortener</h1>
    <form action="/shorten" method="post">
        <label for="long_url">Enter a URL:</label><br>
        <input type="text" id="long_url" name="long_url"><br>
        <input type="submit" value="Shorten">
    </form>
    """

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = secrets.token_urlsafe(6)  # Generate a random 6-character token
    urls[short_url] = long_url
    return f'Shortened URL: {request.host_url}{short_url}'

@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in urls:
        return redirect(urls[short_url])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
