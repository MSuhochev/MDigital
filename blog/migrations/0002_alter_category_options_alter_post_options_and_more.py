# Generated by Django 5.0.4 on 2024-04-17 13:38

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Пост", "verbose_name_plural": "Посты"},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "Тег", "verbose_name_plural": "Теги"},
        ),
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default=None, max_length=200, unique=True, verbose_name="Слаг"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="blog.category",
                verbose_name="Родительская категория",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(max_length=100, unique=True, verbose_name="Слаг"),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="post",
                to="blog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(upload_to="articles/", verbose_name="Изображение"),
        ),
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(
                related_name="posts", to="blog.tag", verbose_name="Теги"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(verbose_name="Текст"),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Заголовок"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(max_length=100, unique=True, verbose_name="Слаг"),
        ),
    ]
