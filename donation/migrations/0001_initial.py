# Generated by Django 5.0.3 on 2024-03-15 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('bill', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donater', models.CharField(blank=True, max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('text', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('acceptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='donation.acceptor')),
            ],
        ),
    ]
