# Generated by Django 4.0.1 on 2022-02-19 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_auth_isauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('resume', models.CharField(max_length=300)),
                ('avatar', models.CharField(max_length=300)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.auth')),
            ],
        ),
    ]
