from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . import models
from .models import Post, Comment


# Create your views here.
def home(request):
    PostObjectList = models.Post.objects
    context = {"PostObjectList" : PostObjectList}
    return render(request, 'home.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    newPostObject = models.Post()
    newPostObject.title = request.POST['title']
    newPostObject.pub_date = timezone.datetime.now()
    newPostObject.body = request.POST['body']
    newPostObject.save()
    return redirect('home')

def detail(request, post_id):
    detailPostObject = get_object_or_404(models.Post, pk=post_id)
    if request.method == 'POST':
        newCommentObject = models.Comment()
        newCommentObject.parentClassObject = detailPostObject
        newCommentObject.comment_title = request.POST['comment_title']
        newCommentObject.comment_pub_date = timezone.datetime.now()
        newCommentObject.comment_body = request.POST['comment_body']
        newCommentObject.save()
    context = {"detailPostObject" : detailPostObject }
    return render(request, 'detail.html', context)

def update(request, post_id):
    updatePostObject = get_object_or_404(models.Post, pk=post_id)
    if request.method == 'POST':
        updatePostObject.title = request.POST['title']
        updatePostObject.pub_date = timezone.datetime.now()
        updatePostObject.body = request.POST['body']
        updatePostObject.save()
        return redirect('/detail/'+str(post_id))
    context = {"updatePostObject" : updatePostObject}
    return render(request, 'update.html', context)

def delete(request, post_id):
    deletePostObject = get_object_or_404(models.Post, pk=post_id)
    deletePostObject.delete()
    return redirect('home')

def commentDelete(request, post_id, comment_id):
    deleteCommentObject = get_object_or_404(models.Comment, pk=comment_id)
    deleteCommentObject.delete()
    return redirect('/detail/' + str(post_id))