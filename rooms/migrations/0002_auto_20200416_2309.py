# Generated by Django 3.0.3 on 2020-04-16 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('abstractitems_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rooms.AbstractItems')),
            ],
            options={
                'abstract': False,
            },
            bases=('rooms.abstractitems',),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(blank=True, to='rooms.RoomType'),
        ),
    ]
