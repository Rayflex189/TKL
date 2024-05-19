# Generated by Django 5.0.4 on 2024-05-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('T_K_L', '0004_details_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Recipients_IBAN',
            field=models.CharField(default='DE31269513110168360295', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='Total_Transfer_Amount',
            field=models.CharField(default='Current Total transfer amount', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='estimated_delivery_time',
            field=models.CharField(default='time duration of funds unlocking proccess', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='recipent_country',
            field=models.CharField(default='Current country name', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='recipent_name',
            field=models.CharField(default='Current Recipients name', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='senders_bank',
            field=models.CharField(default='Current senders bank name', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='senders_country',
            field=models.CharField(default='Current senders country name', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='senders_name',
            field=models.CharField(default='Current senders name', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='status_text',
            field=models.CharField(default='current overhead or current payments due', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='status_update',
            field=models.CharField(default='In progress', max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='transaction',
            field=models.CharField(default='Current transaction name', max_length=200),
        ),
    ]
