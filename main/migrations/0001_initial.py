# Generated by Django 2.2.7 on 2019-11-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('AccountId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('AccountName', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('Title', models.CharField(max_length=200)),
                ('Dates', models.DateField(auto_now=True)),
                ('CategoryId', models.IntegerField()),
                ('AccountId', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('Title', models.CharField(max_length=200)),
                ('Dates', models.DateField(auto_now=True)),
                ('CategoryId', models.IntegerField()),
                ('AccountId', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Bills',
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('BudgetId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('CategoryId', models.IntegerField()),
                ('Dates', models.DateField(auto_now=True)),
                ('Amount', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Budgets',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('CategoryName', models.CharField(max_length=200)),
                ('Level', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('TotalId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('AccountId', models.IntegerField()),
                ('Dates', models.DateField(auto_now=True)),
                ('Totals', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Totals',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=200)),
                ('LastName', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Currency', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
    ]
