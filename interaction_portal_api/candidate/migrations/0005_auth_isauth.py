# Generated by Django 4.0.1 on 2022-02-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='isAuth',
            field=models.BooleanField(default=False),
        ),
    ]