import json


class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        """Возвращает список постов"""
        with open(self.path, "r", encoding="utf-8") as file:
            posts = json.load(file)
        return posts

    def search_posts(self, subline):
        """Возвращает список постов по введённой подстроке
        Args:
            subline: искомая подстрока
        Returns:
            posts: список постов по введённой подстроке"""
        posts = []
        for post in self.load_posts():
            if subline.lower() in post["content"].lower():
                posts.append(post)
        return posts

    def add_content(self, pic, content):
        """Возвращает список всех постов, добавляет к ним новый пост
                Args:
                    pic: имя картинки
                    content: текст поста
                Returns:
                    posts: список всех постов"""
        with open(self.path, "r+", encoding="utf-8") as file:
            posts = json.load(file)
            posts.append({"pic": f"./uploads/images/{pic}", "content": content})
            file.seek(0)
            posts = json.dumps(posts, ensure_ascii=False, indent=4)
            file.write(posts)
        return posts
