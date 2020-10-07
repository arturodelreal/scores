# Generated by Django 3.0.10 on 2020-10-07 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_auto_20201007_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeputyVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.IntegerField(choices=[(0, 'En Contra'), (1, 'Afirmativo'), (2, 'Abstención'), (3, 'Dispensado'), (4, 'No Vota')], null=True)),
                ('deputy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Deputy')),
                ('votation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.DeputyVotation')),
            ],
        ),
    ]
