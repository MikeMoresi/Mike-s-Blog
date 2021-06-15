from django.urls import path
from . import views
from .views import SingUpView

urlpatterns = [

    path('Post',views.postList,name ='postList'),
    path('singUp', SingUpView.as_view(), name='singUp'),
    path('', SingUpView.as_view(), name = 'singUp'),
    path('Post/new/', views.postNew, name='postNew'),
    path('numberOfPosts', views.numberOfPosts, name='numberOfPosts'),
    path('<username>/<id>', views.profile, name='profile'),
    path('postLastHour',views.postLastHour, name='postLastHour'),
    path('search/', views.search, name='search'),
    path('index/',views.index, name='index'),
]