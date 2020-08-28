# Generated by Django 3.1 on 2020-08-28 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Spl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='spls', to='dailymed.set')),
            ],
        ),
        migrations.CreateModel(
            name='Ndc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=15)),
                ('spl', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ndcs', to='dailymed.spl')),
            ],
        ),
    ]