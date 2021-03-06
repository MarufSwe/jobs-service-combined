# Generated by Django 3.0.6 on 2020-05-30 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('job_level', models.CharField(blank=True, choices=[('ENT', 'ENTRY'), ('MID', 'MID'), ('EXP', 'EXPERT')], max_length=20, null=True)),
                ('job_responsibilities', models.TextField(blank=True, max_length=2000, null=True)),
                ('job_location', models.CharField(blank=True, max_length=100, null=True)),
                ('no_of_vacancies', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('employer_id', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('employer_information', models.TextField(blank=True, max_length=500, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('FT', 'FULL_TIME'), ('PT', 'PART_TIME'), ('CT', 'CONTRACTUAL')], max_length=20, null=True)),
                ('employer_location', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')], max_length=20, null=True)),
                ('skill', models.TextField(blank=True, max_length=1000, null=True)),
                ('experience', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('training', models.TextField(blank=True, max_length=500, null=True)),
                ('salary', models.FloatField(blank=True, default=0.0, null=True)),
                ('compensation_and_other_benefits', models.TextField(blank=True, max_length=500, null=True)),
                ('application_deadline', models.DateTimeField(auto_now_add=True, null=True)),
                ('resume_receiving_option', models.CharField(blank=True, choices=[('EM', 'EMAIL'), ('ON', 'ONLINE'), ('HC', 'HARD_COPY')], default='EM', max_length=20, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Category')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='JobTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seeker_id', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('seeker_name', models.CharField(blank=True, max_length=100, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
            ],
            options={
                'verbose_name_plural': 'Job tracking',
                'unique_together': {('job', 'seeker_id')},
            },
        ),
    ]
