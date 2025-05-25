"""
URL configuration for TODO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todoapp import views
from portfolio import views as portfolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('todo_list',views.todo_list,name='todo_list'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),
    path('update_todo/<int:id>/', views.update_todo, name='update_todo'),
    path('complete_todo/<int:id>/', views.complete_todo, name='complete_todo'),
    path('index/',portfolio_views.index,name='index'),
]
