from flask import Blueprint, render_template, request
from functions import PostHandler
import logging
from json import JSONDecodeError


main_blueprint = Blueprint('main_blueprint', __name__)
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding='utf-8')


@main_blueprint.route('/')
def profile_page():
    """Главная страница"""
    return render_template('index.html')


@main_blueprint.route("/search")
def search_page():
    """Страница поиска"""
    s = request.args.get("s")
    logging.info(f"выполнен поиск по запросу '{s}'")
    try:
        posts = PostHandler("posts.json")
        posts = posts.search_posts(s)
        return render_template("post_list.html", posts=posts, query=s)
    except FileNotFoundError or JSONDecodeError:
        return "ошибка загрузки"
