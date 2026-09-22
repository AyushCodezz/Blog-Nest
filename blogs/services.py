from .models import Post


def get_all_posts():
    return Post.objects.select_related("author").order_by("-created_at")


def get_post_by_id(post_id):
    return Post.objects.select_related("author").get(id=post_id)


def create_post(title, content, author):
    return Post.objects.create(
        title=title,
        content=content,
        author=author,
    )


def update_post(post, title, content):
    post.title = title
    post.content = content
    post.save()

    return post


def delete_post(post):
    post.delete()