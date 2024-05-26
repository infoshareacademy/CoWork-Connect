# Generated by Django 5.0.2 on 2024-05-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coapp', '0006_serviceterm_description_3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='logos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ServiceTerm',
        ),
    ]
