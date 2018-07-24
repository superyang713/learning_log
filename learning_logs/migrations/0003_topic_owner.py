# Generated by Django 2.0.7 on 2018-07-24 21:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=True, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
