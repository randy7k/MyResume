# Generated by Django 4.0.2 on 2022-03-08 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Portfolio'},
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='Portfolio.category'),
        ),
    ]
