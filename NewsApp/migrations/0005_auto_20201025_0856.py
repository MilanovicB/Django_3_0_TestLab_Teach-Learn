# Generated by Django 3.1.2 on 2020-10-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0004_registrationdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdata',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]