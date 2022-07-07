from flask import Flask,render_template
import requests
app = Flask(__name__)
app.secret_key =  "secretKey"

@app.route('/')
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=general&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('index.html',cases = case)


@app.route('/tech')

def tech():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('tech.html',cases = case)

@app.route('/business')

def business():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('business.html',cases = case)


@app.route('/health')

def health():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=health&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('health.html',cases = case)

@app.route('/science')

def science():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('science.html',cases = case)


@app.route('/entertainment')

def entertainment():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('entertainment.html',cases = case)

@app.route('/sports')

def sports():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&pageSize=55&apiKey=5fc954292bea4b7c8ddbf33907316b8d"
    r = requests.get(url).json()
    case = {

        'articles':r['articles']

    }
    return render_template('sport.html',cases = case)

if __name__ == '__main__':
    app.run(debug=True)

