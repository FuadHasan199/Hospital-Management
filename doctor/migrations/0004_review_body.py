# Generated by Django 5.0.6 on 2024-06-20 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='body',
            field=models.TextField(default='very good doctor i have seen in my life'),
        ),
    ]
