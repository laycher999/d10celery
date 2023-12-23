import datetime

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, Category
from News_Portal import settings


@shared_task
def send_mail_subscriber(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    subscribers: list[str] = []
    title = post.post_name
    for category in categories:
        subscribers += category.subscribers.all()
    subscribers_emails = [s.email for s in subscribers]
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': post.preview(),
            'link': f'{settings.SITE_URL}news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@shared_task
def send_weekly_mail():
    start_date = datetime.datetime.today() - datetime.timedelta(days=6)
    this_weeks_posts = Post.objects.filter(post_time__gt=start_date)
    for cat in Category.objects.all():
        post_list = this_weeks_posts.filter(category=cat)
        if post_list:
            subscribers = cat.subscribers.values('username', 'email')
            subscribers_emails = []
            for sub in subscribers:
                subscribers_emails.append(sub['email'])

            html_content = render_to_string(
                'daily_post.html', {
                    'link': settings.SITE_URL + 'news/',
                    'posts': post_list,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Категория - {cat.category_name}',
                body="---------",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=subscribers_emails
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
    print('Рассылка произведена!')
