from ast import Break
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post, User_Report

# Create your views here.

def index(request):
    Posts = Post.objects.all()
    context = {'Posts' : Posts}
    return render(request,'general_app/index.html',context)
def lastest(request):
    Posts = Post.objects.order_by('-id')
    context = {'Posts' : Posts}
    return render(request,'general_app/lastest.html',context)
def languages(request):
    Posts = Post.objects.all()
    context = {'Posts' : Posts}
    return render(request,'general_app/languages/languages.html',context)
def english(request):
    Posts = Post.objects.filter(language='English')
    context = {'Posts' : Posts}
    return render(request,'general_app/languages/english.html',context)
def khmer(request):
    Posts = Post.objects.filter(language='Khmer')
    context = {'Posts' : Posts}
    return render(request,'general_app/languages/khmer.html',context)
def thai(request):
    Posts = Post.objects.filter(language='Thai')
    context = {'Posts' : Posts}
    return render(request,'general_app/languages/thai.html',context)
def chinese(request):
    Posts = Post.objects.filter(language='Chinese')
    context = {'Posts' : Posts}
    return render(request,'general_app/languages/chinese.html',context)
def post(request,post_url):
    post = Post.objects.get(pk=post_url)
    context = {'post': post}
    return render(request,'general_app/post.html',context)
def result(request):
    try:
        if request.method == 'GET':
            search_query = request.GET['search-query']
            if search_query != "":
                Posts = Post.objects.filter(title__icontains=search_query)
            else:
                Posts = None
            context = {
                'Posts' : Posts,
                'search_query': search_query
            }
            return render(request,'general_app/result.html',context)
    except:
        return HttpResponseRedirect('/')
def report(request):
    if request.method == 'POST':
        Email = request.POST.get('report_email')
        Report = request.POST.get('report_text')
        if Email and Report:
            user_report = User_Report()
            user_report.email = Email
            user_report.report = Report
            user_report.save()
            # return HttpResponseRedirect('thank')
            return render(request,'general_app/thank.html')
    else:
        return render(request,'general_app/report.html')