# Generated by Django 2.1.4 on 2019-05-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_resident_resident_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_telephone',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='resident_telephone',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_telephone',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]