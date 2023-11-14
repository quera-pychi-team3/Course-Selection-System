# Generated by Django 4.2.7 on 2023-11-12 13:40

from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='classes_end_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='classes_start_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='emergency_cancellation_end_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='exams_start_time',
            field=django_jalali.db.models.jDateField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='professors',
            field=models.ManyToManyField(blank=True, related_name='term_professor', to='accounts.professor'),
        ),
        migrations.AlterField(
            model_name='term',
            name='selection_end_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='selection_start_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='term_student', to='accounts.student'),
        ),
        migrations.AlterField(
            model_name='term',
            name='term_end_time',
            field=django_jalali.db.models.jDateField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='update_end_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
        migrations.AlterField(
            model_name='term',
            name='update_start_time',
            field=django_jalali.db.models.jDateTimeField(),
        ),
    ]
