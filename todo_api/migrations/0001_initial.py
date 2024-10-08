# Generated by Django 5.1.1 on 2024-09-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('tarefa', models.CharField(max_length=250)),
                ('data', models.DateField()),
                ('concluida', models.BooleanField()),
            ],
        ),
    ]
