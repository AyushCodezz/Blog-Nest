from django.shortcuts import render

from blogs.services import get_all_posts


def home(request):
    posts = get_all_posts()[:5]

    return render(
        request,
        "home.html",
        {"posts": posts},
    )