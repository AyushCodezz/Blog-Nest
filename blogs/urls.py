from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.post_list,
        name="post_list",
    ),
    path(
        "post/<int:post_id>/",
        views.post_detail,
        name="post_detail",
    ),
    path(
        "post/create/",
        views.create_post_view,
        name="post_create",
    ),
    path(
        "post/<int:post_id>/edit/",
        views.edit_post,
        name="post_edit",
    ),
    path(
        "post/<int:post_id>/delete/",
        views.delete_post,
        name="post_delete",
    ),
]