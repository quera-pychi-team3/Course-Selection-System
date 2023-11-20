# Generated by Django 4.2.4 on 2023-11-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationupdate',
            name='approval_status',
            field=models.CharField(choices=[['E', 'درحال انجام توسط دانشجو'], ['P', 'منتظر نظر استاد'], ['A', 'تایید شده'], ['D', 'رد شده']], default='E', max_length=1),
        ),
    ]
