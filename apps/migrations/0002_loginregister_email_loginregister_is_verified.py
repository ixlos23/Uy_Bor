# Generated by Django 5.1.1 on 2024-09-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginregister',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loginregister',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
