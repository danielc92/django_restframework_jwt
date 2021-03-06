# Generated by Django 2.2.2 on 2019-06-17 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0004_auto_20190617_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('languages', models.ManyToManyField(to='languages.Language')),
            ],
        ),
    ]
