from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post
from .services import (
    create_post,
    delete_post as delete_post_service,
    get_all_posts,
    get_post_by_id,
    update_post,
)


def post_list(request):
    posts = get_all_posts()

    return render(
        request,
        "blogs/post_list.html",
        {"posts": posts},
    )


def post_detail(request, post_id):
    post = get_post_by_id(post_id)

    return render(
        request,
        "blogs/post_details.html",
        {"post": post},
    )


@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            create_post(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
                author=request.user,
            )

            return redirect("post_list")
    else:
        form = PostForm()

    return render(
        request,
        "blogs/post_form.html",
        {"form": form},
    )


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect("post_detail", post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            update_post(
                post=post,
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"],
            )

            return redirect("post_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blogs/post_form.html",
        {
            "form": form,
            "post": post,
        },
    )


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect("post_detail", post_id=post.id)

    if request.method == "POST":
        delete_post_service(post)

        return redirect("post_list")

    return render(
        request,
        "blogs/post_confirm_delete.html",
        {"post": post},
    )