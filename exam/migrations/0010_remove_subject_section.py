# Generated by Django 2.0.6 on 2018-08-31 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_subject_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='Section',
        ),
    ]
