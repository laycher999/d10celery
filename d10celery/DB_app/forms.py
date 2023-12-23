from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from datetime import datetime, timedelta
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_name',
            'post_text',
            'author',
            'category',
        ]
        labels = {
            'post_name': 'Заголовок',
            'post_text': 'Текст',
            'author': 'Автор',
            'category': 'Категория',
        }

    def clean(self):
        cleaned_data = super().clean()
        post_text = cleaned_data.get('post_text')
        if post_text is not None and len(post_text) < 30:
            raise ValidationError({
                'post_text': "Текст поста не может быть менее 30 символов."
            })

        post_name = cleaned_data.get('post_name')
        if post_name == post_text:
            raise ValidationError({
                'post_text': "Текст поста не должен быть идентичным названию."
            })

        # post_time = datetime.now()
        # author = cleaned_data.get('author')
        # if len([post for post in Post.objects.filter(author=author) if
        #         post_time > (datetime.now() - timedelta(days=1))]) > 2:
        #     raise ValidationError({
        #         'post_text': "Разрешено публиковать не более 3 постов в сутки."
        #     })
        return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        return user
