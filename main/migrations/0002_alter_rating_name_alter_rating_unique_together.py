# Generated by Django 5.0.6 on 2024-08-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='name',
            field=models.CharField(blank=True, default='user', max_length=250),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('product', 'name')},
        ),
    ]
