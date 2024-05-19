# Generated by Django 5.0.2 on 2024-05-19 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_number', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('monitor_number', models.IntegerField(null=True)),
                ('power_socket_count', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OurOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description_1_subtitle', models.TextField(default='Insert your title for first paragraph...')),
                ('description_1', models.TextField(default="Insert your first paragraph's description...")),
                ('description_2_subtitle', models.TextField(blank=True, default='')),
                ('description_2', models.TextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coapp.desk')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
