# Generated by Django 3.1.4 on 2021-07-04 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='certificate',
        ),
        migrations.DeleteModel(
            name='project',
        ),
        migrations.DeleteModel(
            name='sop',
        ),
    ]
