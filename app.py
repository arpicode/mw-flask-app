from flask import Flask, render_template

app = Flask(__name__)

# Run app server in debug mode
SERVER_DEBUG = True


@app.route("/")
def home() -> str:
    return render_template('home.html.j2')


@app.route("/about")
def about() -> str:
    return render_template('about.html.j2')


@app.route('/articles')
def articles() -> str:
    return render_template('articles.html.j2')


if __name__ == '__main__':
    app.run(debug=SERVER_DEBUG)
