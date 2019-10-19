# Generated by Django 2.2.6 on 2019-10-19 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index101',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_one', models.IntegerField(verbose_name='data one')),
                ('data_two', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='data two')),
                ('calculated_value', models.CharField(blank=True, max_length=32, verbose_name='calculated value')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commons.Description')),
            ],
            options={
                'ordering': ['id'],
                'permissions': [('index_manager', 'Index Manager')],
            },
        ),
    ]
