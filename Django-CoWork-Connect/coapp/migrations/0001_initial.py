# Generated by Django 5.0.3 on 2024-04-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Desk",
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
                ("desk_type", models.CharField(max_length=255)),
                ("monitor", models.BooleanField(default=False)),
                ("size", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("status", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
            ],
        ),
    ]