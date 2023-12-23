# Задачи выполняются с помощью celery!
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
#
# from News_Portal import settings
# from .models import PostCategory

# def send_notifications(preview, pk, title, subscribers):
#     html_context = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}news/{pk}'
#         }
#     )
#     print(preview)
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#
#     msg.attach_alternative(html_context, 'text/html')
#     msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#         subscribers_emails = [s.email for s in subscribers]
#         send_notifications(str(instance.post_text)[:50]+'...', instance.pk, instance.post_name, subscribers_emails)
