# Generated by Django 4.0.2 on 2022-02-19 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_socialnetwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetwork',
            name='source',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='social_networks', to='src.source'),
        ),
    ]
