from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post, Category
from django import forms


class PostFilter(FilterSet):
    post_name = CharFilter(lookup_expr='icontains', label='Заголовок содержит...')
    author__author__username = CharFilter(lookup_expr='icontains', label='Имя автора (username) содержит...')
    post_time = DateFilter(field_name='post_time', lookup_expr='gt',
                           widget=forms.DateInput(attrs={'type': 'date'}), label='Дата публикации позже, чем...')

    class Meta:
        model = Post
        fields = ['post_name', 'author__author__username', 'post_time']
