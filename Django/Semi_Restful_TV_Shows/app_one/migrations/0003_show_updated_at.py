# Generated by Django 2.2.4 on 2022-09-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_show_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
