from flask import Flask, render_template
from scraper import get_news

app = Flask(__name__)

@app.route("/")
def home():
    news = get_news()
    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)