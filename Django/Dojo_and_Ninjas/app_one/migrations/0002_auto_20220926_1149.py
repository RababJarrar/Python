# Generated by Django 2.2.4 on 2022-09-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dojo',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='old dojo', max_length=255),
            preserve_default=False,
        ),
    ]
