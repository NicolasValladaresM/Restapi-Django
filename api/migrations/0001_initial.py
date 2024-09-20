# Generated by Django 4.2.16 on 2024-09-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('surname', models.CharField(max_length=400)),
                ('nickname', models.CharField(max_length=400)),
                ('age', models.PositiveSmallIntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
