# Generated by Django 5.0.4 on 2024-05-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_K_L', '0002_rename_transaction_name_details_transaction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='Recipients_IBAN',
            field=models.CharField(default='DE31269513110168360295', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='estimated_delivery_time',
            field=models.CharField(default='time duration of funds unlocking proccess', max_length=20),
        ),
        migrations.AddField(
            model_name='details',
            name='status_text',
            field=models.CharField(default='current overhead or current payments due', max_length=20),
        ),
    ]