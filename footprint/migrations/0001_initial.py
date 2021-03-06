# Generated by Django 2.0.1 on 2019-11-17 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EffectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('resource', models.CharField(choices=[('air', 'air'), ('water', 'water'), ('soil', 'soil')], max_length=10)),
                ('property', models.CharField(choices=[('mass', 'kg')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='effect',
            name='effect_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footprint.EffectType'),
        ),
        migrations.AddField(
            model_name='effect',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footprint.ProductType'),
        ),
    ]
