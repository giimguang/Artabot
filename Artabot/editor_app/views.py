from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from editor_app.utils.activation_token_generator import activation_token_generator
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpRequest
from editor_app.forms import UserProfileForm
from editor_app.forms import RegisterForm,CustomUser
from general_app.models import Post
# Create your views here.

# @login_required
@login_required
def editor(request):
    return render(request,'editor_app/editor.html')
@login_required
def postdb(request):
    posts = Post.objects.all()
    is_saved = request.COOKIES.get("is_saved") == "1"
    flash_message = "The post was changed successfully." if is_saved else None
    context = {
        'posts': posts,
        'flash_message': flash_message
    }
    response = render(request,'editor_app/post_db.html',context)
    if is_saved:
        response.delete_cookie("is_saved")
    return response
@login_required
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
@login_required
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
            respone = HttpResponseRedirect('/editor/postdb')
            respone.set_cookie("is_saved","1")
            return respone
    else:
        context = {
            'post': post,
        }
        return render(request,'editor_app/edit-post.html',context)
@login_required
def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('/editor/postdb')
    else:
        return render(request,'editor_app/delete-post.html')

def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register and wait for activation
            user: CustomUser = form.save(commit=False)
            user.is_active = False
            user.save()

            # Build email body
            context = {
                "protocol": request.scheme,
                "host": request.get_host(),
                "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
                "token": activation_token_generator.make_token(user),
            }
            email_body = render_to_string(
                "editor_app/activate_email.html", context=context
            )

            # Send email
            email = EmailMessage(
                to=[user.email],
                subject="Activate account หน่อยครับ",
                body=email_body,
            )
            email.send()

            # Change redirect to register thank you
            return HttpResponseRedirect(reverse("register_thankyou"))
    else:
        form = RegisterForm()

    # GET
    context = {"form": form}
    return render(request, "editor_app/register.html", context)

def register_thankyou(request: HttpRequest):
    return render(request, "editor_app/register_thankyou.html")

def activate(request: HttpRequest, uidb64: str, token: str):
    title = "Activate account เรียบร้อย"
    content = "คุณสามารถเข้าสู่ระบบได้เลย"
    id = urlsafe_base64_decode(uidb64).decode()
    try:
        user = CustomUser.objects.get(id=id)
        if not activation_token_generator.check_token(user, token):
            raise Exception("Check token false")
        user.is_active = True
        user.save()
        login(request,user)
    except:
        print("Activate ไม่ผ่าน")
        title = "Activate account ไม่ผ่าน"
        content = "เป็นไปได้ว่าลิ้งค์ไม่ถูกต้อง หรือหมดอายุไปแล้ว"

    context = {"title": title, "content": content}
    return render(request, "editor_app/activate.html", context)

@login_required
def dashboard(request):
    return render(request,'editor_app/dashboard.html')
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request,'editor_app/profile.html',context)