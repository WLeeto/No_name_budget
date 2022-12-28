# Generated by Django 4.1.3 on 2022-12-28 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('summ', models.FloatField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BillsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('plan', models.FloatField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('plan', models.FloatField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('first_name', models.CharField(max_length=125)),
                ('second_name', models.CharField(max_length=125)),
                ('surname', models.CharField(max_length=125)),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='Аватар')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('summ', models.FloatField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('plan', models.FloatField(max_length=500)),
                ('permanent_income', models.BooleanField(default=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.bill')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.category')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.currency')),
            ],
            options={
                'verbose_name': 'Доход',
                'verbose_name_plural': 'Доходы',
            },
        ),
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=125)),
                ('summ', models.FloatField()),
                ('description', models.CharField(max_length=500)),
                ('plan', models.FloatField()),
                ('permanent_cost', models.FloatField()),
                ('bound_cost', models.FloatField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.bill')),
                ('category_cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.categorycost')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.currency')),
            ],
            options={
                'verbose_name': 'Расход',
                'verbose_name_plural': 'Расходы',
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.costs')),
                ('incomes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.incomes')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='bills_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='First.billscategory'),
        ),
    ]