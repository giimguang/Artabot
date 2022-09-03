from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('lastest/',views.lastest,name="lastest"),
    path('languages/',views.languages,name="languages"),
    path('languages/english/',views.english,name="english"),
    path('languages/khmer/',views.khmer,name="khmer"),
    path('languages/thai/',views.thai,name="thai"),
    path('languages/chinese/',views.chinese,name="chinese"),
    path('post/<str:post_url>',views.post,name="post"),
    path('result',views.result,name="result"),
    path('report/',views.report,name="report"),
    path('thank/',views.thank,name="thank")
]