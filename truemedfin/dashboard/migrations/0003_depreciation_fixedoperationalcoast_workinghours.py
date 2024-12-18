# Generated by Django 5.1.3 on 2024-12-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_num_pieces_item_number_of_pieces_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depreciation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Investment_cost', models.IntegerField()),
                ('number_of_years', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FixedOperationalCoast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rent', models.IntegerField()),
                ('Routine_markting', models.IntegerField()),
                ('Bills', models.IntegerField()),
                ('SecretaryAndAssistant', models.IntegerField()),
                ('Doctor_salaries', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_per_day', models.IntegerField()),
                ('days_per_week', models.IntegerField()),
            ],
        ),
    ]
