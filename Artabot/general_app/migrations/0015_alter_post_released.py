# Generated by Django 4.0.7 on 2022-09-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0014_alter_post_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
