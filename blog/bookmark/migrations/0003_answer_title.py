# Generated by Django 3.2 on 2023-01-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
