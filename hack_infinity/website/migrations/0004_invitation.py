# Generated by Django 4.1.6 on 2023-02-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_user_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation', models.TextField(max_length=32, verbose_name='invitation')),
            ],
        ),
    ]