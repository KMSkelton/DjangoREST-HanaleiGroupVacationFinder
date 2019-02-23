# Generated by Django 2.1.7 on 2019-02-20 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=165)),
                ('code', models.CharField(blank=True, max_length=3)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='country.Country')),
            ],
            options={
                'ordering': ('country', 'name'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together={('name', 'country')},
        ),
    ]