# Generated by Django 4.0.3 on 2022-04-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userextension_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='link',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
