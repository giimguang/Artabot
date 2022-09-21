# Generated by Django 4.0.7 on 2022-09-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0010_alter_post_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.CharField(choices=[('chinese', 'Chinese'), ('english', 'English'), ('khmer', 'Khmer'), ('thai', 'Thai')], max_length=50),
        ),
    ]