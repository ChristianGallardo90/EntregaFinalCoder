# Generated by Django 4.2.2 on 2023-07-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/'),
        ),
    ]
