# Generated by Django 4.0.6 on 2022-07-23 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matric_no',
            field=models.CharField(default='2022/29/987AB', max_length=50, unique=True),
        ),
    ]
