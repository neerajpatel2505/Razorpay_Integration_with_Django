# Generated by Django 4.2.7 on 2023-11-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ItemInfo",
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
                ("iten_name", models.CharField(max_length=200)),
                ("item_desc", models.CharField(max_length=200)),
                ("item_price", models.IntegerField()),
                ("item_image", models.ImageField(upload_to="image")),
            ],
        ),
    ]
