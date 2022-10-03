# Generated by Django 4.0.6 on 2022-10-01 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('paternal_lastname', models.CharField(max_length=40)),
                ('maternal_lastname', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='client.usertype')),
            ],
        ),
    ]