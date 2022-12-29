from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    # path('servicies/', views.servicies, name="servicies"),
    path('store/', views.store, name="store"),
    # path('blog/', views.blog, name="blog"),
 
]