# Generated by Django 4.1.2 on 2022-10-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_house_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='House_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='images/'),
        ),
    ]
