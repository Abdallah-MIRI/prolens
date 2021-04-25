from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import MainView, PostJsonListView, about, connect
from home import views

# app_name = 'home'

urlpatterns = [
    # path('', MainView.as_view(), name='home'),
    path('', MainView.as_view(), name='main-view'),
    path('home/<int:num_posts>/', PostJsonListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('connect/', views.connect, name='connect'),
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
