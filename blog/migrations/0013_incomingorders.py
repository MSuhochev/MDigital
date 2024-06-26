# Generated by Django 4.1 on 2024-04-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0012_subscriber"),
    ]

    operations = [
        migrations.CreateModel(
            name="IncomingOrders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site", models.CharField(max_length=200, verbose_name="Сайт")),
                ("email", models.EmailField(max_length=254)),
                (
                    "date_sent",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата отправки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("pending", "Pending"), ("done", "Done")],
                        default="pending",
                        max_length=20,
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заявка на монетизацию",
                "verbose_name_plural": "Заявки на монетизацию",
            },
        ),
    ]
