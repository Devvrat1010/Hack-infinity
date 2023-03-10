# Generated by Django 4.1.6 on 2023-02-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_invitation_confirmation_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateEventInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=32, verbose_name='event_name')),
                ('venue', models.CharField(max_length=32, verbose_name='venue')),
                ('date', models.DateField(default='No', max_length=32, verbose_name='date')),
                ('sub_event', models.CharField(default='No', max_length=32, verbose_name='sub_event')),
                ('time', models.TimeField(default='No', max_length=32, verbose_name='time')),
            ],
        ),
        migrations.AlterField(
            model_name='invitation_confirmation',
            name='Response',
            field=models.CharField(default='No', max_length=32, verbose_name='Response'),
        ),
    ]
