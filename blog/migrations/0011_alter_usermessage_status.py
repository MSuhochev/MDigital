# Generated by Django 4.1 on 2024-04-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0010_alter_usermessage_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermessage",
            name="status",
            field=models.CharField(
                choices=[("pending", "Pending"), ("done", "Done")],
                default="pending",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
