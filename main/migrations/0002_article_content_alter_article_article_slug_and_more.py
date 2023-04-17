# Generated by Django 4.2 on 2023-04-16 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.SlugField(unique=True, verbose_name='Article slug'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Series slug'),
        ),
    ]