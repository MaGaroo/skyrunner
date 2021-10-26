# Generated by Django 3.2.7 on 2021-10-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asgharzadeh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('uid', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='nightname',
            name='end',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nightname',
            name='start',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
