from django.contrib import admin
from django.urls import path
from website.core.views import home, todos, detail, page_ajuda

app_name = 'news'
urlpatterns = [
    path('', home, name='home'),
    path('ajude-o-portal/', page_ajuda, name='page-ajuda'),
    path('<slug:slug>/',  todos, name='todos'),
    path('detail/<slug:slug>/',  detail, name='detail'),

]