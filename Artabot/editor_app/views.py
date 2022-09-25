from email.mime import image
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest
from editor_app.forms import RegisterForm
from general_app.models import Post
# Create your views here.

# @login_required
@staff_member_required
def editor(request):
    return render(request,'editor_app/editor.html')
@staff_member_required
def postdb(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'editor_app/post_db.html',context)
@staff_member_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        lyric = request.POST.get('text_content')
        tag = request.POST.get('editor-tag')
        language = request.POST.get('editor-lang')
        try:
            image = request.FILES['image']
        except:
            image = "default-img.jpg"
        if title and tag and language:
            postModel = Post()
            postModel.title = title
            postModel.artist = artist
            postModel.album = album
            postModel.lyric = lyric
            postModel.tag = tag
            postModel.language = language
            postModel.image = image
            postModel.save()
            return HttpResponseRedirect('/editor/postdb')
    else:
        return render(request,'editor_app/add-post.html')
@staff_member_required
def edit(request,post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        lyric = request.POST.get('text_content')
        tag = request.POST.get('editor-tag')
        language = request.POST.get('editor-lang')
        try:
            image = request.FILES['image']
        except:
            image = post.image
        if title and tag and language:
            postModel = Post.objects.get(id = post_id)
            postModel.title = title
            postModel.artist = artist
            postModel.album = album
            postModel.lyric = lyric
            postModel.tag = tag
            postModel.language = language
            postModel.image = image
            postModel.save()
            return HttpResponseRedirect('/editor/postdb')
    else:
        context = {
        'post': post
        }
        return render(request,'editor_app/edit-post.html',context)
@staff_member_required
def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('/editor/postdb')
    else:
        return render(request,'editor_app/delete-post.html')
def register(request: HttpRequest):
    if request.method == 'POST':
        #Post
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        #Get
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,'editor_app/register.html',context)