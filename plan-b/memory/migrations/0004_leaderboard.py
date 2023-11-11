# Generated by Django 3.1.3 on 2020-12-01 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0003_auto_20201201_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flips', models.CharField(max_length=15)),
                ('time_left', models.CharField(max_length=20)),
                ('Player_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memory.inputmodel')),
            ],
        ),
    ]