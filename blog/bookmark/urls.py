from django.urls import path, include
from django.conf.urls import url
from bookmark.views import *
from . import views

urlpatterns = [
    path('first', BookmarkLV.as_view(), name='index1'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail1'),
    path('answer/', AnswerLV.as_view(), name='index'),
    path('answer/<int:pk>', AnswerDV.as_view(), name='detail'),
    path('answer/create/<int:answer_id>/', views.reply_create, name='reply_create'),
    path('answer/create/', views.answer_create, name='answer_create')
]