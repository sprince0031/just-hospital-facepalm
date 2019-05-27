# Generated by Django 2.2.1 on 2019-05-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentdetails',
            name='appointment_date',
        ),
        migrations.RemoveField(
            model_name='appointmentdetails',
            name='appointment_time',
        ),
        migrations.RemoveField(
            model_name='appointmentdetails',
            name='reason_for_consultation',
        ),
        migrations.AddField(
            model_name='patientsteggeddetails',
            name='appointment_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patientsteggeddetails',
            name='appointment_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='patientsteggeddetails',
            name='reason_for_consultation',
            field=models.CharField(max_length=300, null=True),
        ),
    ]