# Generated by Django 3.2.18 on 2023-04-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('q_name', models.CharField(max_length=2555)),
                ('answer', models.CharField(max_length=2555)),
            ],
        ),
    ]
