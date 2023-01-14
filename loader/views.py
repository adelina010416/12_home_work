import logging
from flask import Blueprint, render_template, request
from functions import PostHandler
from json import JSONDecodeError


loader_blueprint = Blueprint('loader_blueprint', __name__)
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding='utf-8')


@loader_blueprint.route("/post")
def page_post_form():
    """Страничка добавления нового поста"""
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    """Страничка после добавления нового поста"""
    allowed_expansion = ["png", "jpg", "jpeg", "bmp"]
    try:
        picture = request.files.get("picture")
        content = request.form.get("content")
        filename = picture.filename
        expansion = filename.split(".")[-1]
        if not picture:
            logging.error("ошибка загрузки")
            return "не удалось загрузить картинку"
        if expansion.lower() not in allowed_expansion:
            logging.info(f'попытка загрузить файл с расширением "{expansion}"')
            return f"формат {expansion} не поддерживается"
        picture.save(f"./uploads/images/{filename}")
        try:
            posts = PostHandler("posts.json")
            posts.add_content(filename, content)
            return render_template('post_uploaded.html', pic=f"./uploads/images/{filename}", content=content)
        except FileNotFoundError or FileExistsError or JSONDecodeError as e:
            logging.error(f"ошибка загрузки типа {e}")
            return f"посты потерялись :(<br>файл не найден"
    except Exception as e:
        logging.error(f"ошибка загрузки типа {e}")
        return "Ошибка загрузки"
