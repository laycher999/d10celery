# Задача выполняется с помощью celery!
# import logging
# import datetime
#
# from django.conf import settings
#
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
# from django.core.mail import EmailMultiAlternatives
# from django.core.management.base import BaseCommand
# from django.template.loader import render_to_string
# from django_apscheduler.jobstores import DjangoJobStore
# from django_apscheduler.models import DjangoJobExecution
#
# logger = logging.getLogger(__name__)
#
# from DB_app.models import Post, Category
# from News_Portal import settings
#
#
# def my_job():
#     start_date = datetime.datetime.today() - datetime.timedelta(days=6)
#     this_weeks_posts = Post.objects.filter(post_time__gt=start_date)
#     for cat in Category.objects.all():
#         post_list = this_weeks_posts.filter(category=cat)
#         if post_list:
#             subscribers = cat.subscribers.values('username', 'email')
#             recipients = []
#             for sub in subscribers:
#                 recipients.append(sub['email'])
#             html_content = render_to_string(
#                 'daily_post.html', {
#                     'link': settings.SITE_URL + 'news/',
#                     'posts': post_list,
#                 }
#             )
#
#             msg = EmailMultiAlternatives(
#                 subject=f'Категория - {cat.category_name}',
#                 body="---------",
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 to=recipients
#             )
#             msg.attach_alternative(html_content, 'text/html')
#             msg.send()
#     print('рассылка произведена')
#
#
# def delete_old_job_executions(max_age=604_800):
#     """This job deletes all apscheduler job executions older than `max_age` from the database."""
#     DjangoJobExecution.objects.delete_old_job_executions(max_age)
#
#
# class Command(BaseCommand):
#     help = "Runs apscheduler."
#
#     def handle(self, *args, **options):
#         scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
#         scheduler.add_jobstore(DjangoJobStore(), "default")
#
#         scheduler.add_job(
#             my_job,
#             trigger=CronTrigger(second="*/10"),
#             id="my_job",
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info("Added job 'my_job'.")
#
#         scheduler.add_job(
#             delete_old_job_executions,
#             trigger=CronTrigger(
#                 day_of_week="mon", hour="00", minute="00"
#             ),
#             id="delete_old_job_executions",
#             max_instances=1,
#             replace_existing=True,
#         )
#         logger.info(
#             "Added weekly job: 'delete_old_job_executions'."
#         )
#
#         try:
#             logger.info("Starting scheduler...")
#             scheduler.start()
#         except KeyboardInterrupt:
#             logger.info("Stopping scheduler...")
#             scheduler.shutdown()
#             logger.info("Scheduler shut down successfully!")
