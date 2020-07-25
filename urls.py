"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import myapp.views #url요청을 view에 연결

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', myapp.views.index, name = 'index'), #path 이름도 정의해주자
    path('blog/', myapp.views.blog, name = 'blog'),
    path('detail/<int:blog_id>/', myapp.views.detail, name = 'detail'),
    path('new/', myapp.views.new, name = 'new'),
    path('create/', myapp.views.create, name = 'create'),
    path('edit/<int:blog_id>/', myapp.views.edit, name = 'edit'),
    path('update/<int:blog_id>/', myapp.views.update, name = 'update'),
    path('delete/<int:blog_id>/', myapp.views.delete, name = 'delete'),
]
