# Generated by Django 3.0.10 on 2020-10-06 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalGroup',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(choices=[('red', 'red')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Deputy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Hombre'), ('F', 'Mujer')], max_length=1)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('political_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.PoliticalGroup')),
            ],
        ),
    ]