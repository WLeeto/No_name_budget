# Generated by Django 4.1.3 on 2022-12-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='budget',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='First.budget'),
        ),
    ]