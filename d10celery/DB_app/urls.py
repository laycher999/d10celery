from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryList, be_author, subscribe

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('articles/create/', PostCreate.as_view(), name='post_create'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('be_author/', be_author, name='be_author'),
    path('categories/<int:pk>/', CategoryList.as_view(), name='category_posts_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
