# Generated by Django 4.0.7 on 2022-09-15 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0016_alter_post_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
