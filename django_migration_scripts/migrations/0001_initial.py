# Generated by Django 3.0.3 on 2020-09-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MigrationScripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('migration_name', models.CharField(max_length=255)),
                ('applied', models.BooleanField(default=False)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]