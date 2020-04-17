# Generated by Django 2.1.4 on 2019-05-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appoint',
            old_name='IsRead',
            new_name='doctor_IsRead',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='is_read',
            new_name='doctor_IsRead',
        ),
        migrations.AddField(
            model_name='appoint',
            name='resident_IsRead',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='resident_IsRead',
            field=models.CharField(max_length=20, null=True),
        ),
    ]