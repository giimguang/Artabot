# Generated by Django 4.0.7 on 2022-09-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_app', '0011_alter_post_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='released',
            field=models.DateField(blank=True, max_length=50, null=True),
        ),
    ]
