# Generated by Django 4.1.2 on 2022-11-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='info',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='about',
            field=models.CharField(max_length=1024),
        ),
    ]