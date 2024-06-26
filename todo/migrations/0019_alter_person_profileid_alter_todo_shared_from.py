# Generated by Django 4.2.13 on 2024-06-15 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_alter_person_profileid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileId',
            field=models.CharField(default='899ca3dd-707e-4ac6-8f83-2838c3491f0d', max_length=255),
        ),
        migrations.AlterField(
            model_name='todo',
            name='shared_from',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='shared_from', to=settings.AUTH_USER_MODEL),
        ),
    ]
