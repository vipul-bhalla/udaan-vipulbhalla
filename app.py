from flask import Flask
    # redirect, url_for
from flask import request
import requests
from flask import render_template
l=[]
r = requests.get(url='https://newsapi.org/v2/top-headlines?apiKey=cd1db87dec794c2288c915ba6abeee94&country=in')
x=r.json()
x=x['articles']
for i in x:
    l.append(i['title'].lower())

class FlaskIgnite:

    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template("index.html")

    @app.route('/result', methods=['POST'])
    def result():
        text = request.form['text']
        text=text.lower()
        res=[]
        for i in l:
            if text in i:
                print(i)
                res.append(i)

        return render_template("new_resultList.html", tfr=res)

    if __name__ == '__main__':
        app.run()


Ignite=FlaskIgnite()
Ignite.my_form()
Ignite.result()