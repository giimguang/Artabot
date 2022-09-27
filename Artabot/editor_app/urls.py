from django.urls import path,include
from . import views
urlpatterns = [
    path('',include("django.contrib.auth.urls")),
    path('',views.editor,name='editor'),
    path('register/',views.register,name='register'),
    path('register/thankyou',views.register_thankyou,name='register_thankyou'),
    path("activate/<str:uidb64>/<str:token>", views.activate, name="activate"),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('postdb/',views.postdb,name='postdb'),
    path('postdb/add/',views.add,name='add'),
    path('postdb/delete/<str:post_id>',views.delete,name='delete'),
    path('postdb/edit/<str:post_id>',views.edit,name='edit'),
]
