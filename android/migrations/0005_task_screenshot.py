# Generated by Django 3.2 on 2021-04-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android', '0004_auto_20210414_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='screenshot',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]