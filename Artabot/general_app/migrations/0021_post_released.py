# Generated by Django 4.0.7 on 2022-09-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0020_remove_post_released'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='released',
            field=models.DateField(blank=True, null=True),
        ),
    ]
