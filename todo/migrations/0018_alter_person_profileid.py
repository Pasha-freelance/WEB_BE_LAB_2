# Generated by Django 4.2.13 on 2024-06-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_rename_sharedfrom_todo_shared_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileId',
            field=models.CharField(default='24dae28a-8c30-4672-b257-261d019d327b', max_length=255),
        ),
    ]
