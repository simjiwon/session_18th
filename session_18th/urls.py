from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('new/', blog.views.new, name="new"),
    path('create/', blog.views.create, name="create"),
    path('detail/<int:post_id>', blog.views.detail, name="detail"),
    path('update/<int:post_id>', blog.views.update, name="update"),
    path('delete/<int:post_id>', blog.views.delete, name="delete"),
    path('commentDelete/<int:post_id>/<int:comment_id>', blog.views.commentDelete, name="commentDelete"),
]