# Generated by Django 2.2.1 on 2019-05-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0002_appointmentdetails_appointment_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientsteggeddetails',
            name='patient_DOB',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='patientsteggeddetails',
            name='patient_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patientsteggeddetails',
            name='reason_for_consultation',
            field=models.CharField(max_length=300, null=True),
        ),
    ]