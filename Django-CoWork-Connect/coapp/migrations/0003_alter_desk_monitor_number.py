# Generated by Django 5.0.3 on 2024-05-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coapp", "0002_rename_name_desk_stock_number_remove_desk_desk_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="desk",
            name="monitor_number",
            field=models.IntegerField(default=1),
        ),
    ]
