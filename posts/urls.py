from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:post_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:post_id>/comments/<int:id>/comment_edit/', views.comment_edit, name='comment_edit'),

    path('<int:post_id>/like/', views.like, name='like'),
    path('<int:post_id>/like-async/', views.like_async, name='like_async'),
]