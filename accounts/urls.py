from . import views
from django.urls import path
from.views import Home, Detail, CreatePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('post/', CreatePost.as_view(success_url='/details'), name='post'),
    path('accounts/<int:pk>/', Detail.as_view(), name='detail'),
    path('details', views.ldetail, name='ldetail')
]
