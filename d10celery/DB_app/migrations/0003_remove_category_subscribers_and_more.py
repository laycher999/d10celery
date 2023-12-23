# Generated by Django 4.2.7 on 2023-11-27 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DB_app', '0002_alter_comment_comment_text_alter_post_post_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
        migrations.DeleteModel(
            name='CategorySubscriber',
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
