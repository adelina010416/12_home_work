from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(loader_blueprint, url_prefix='/')


@app.route("/list")
def page_tag():
    pass


if __name__ == "__main__":
    app.run(debug=True)
