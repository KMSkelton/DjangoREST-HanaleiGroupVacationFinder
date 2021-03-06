# Generated by Django 2.1.7 on 2019-02-20 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=165)),
                ('postal_code', models.CharField(blank=True, max_length=10)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localities', to='state.State')),
            ],
            options={
                'verbose_name_plural': 'Localities',
                'ordering': ('state', 'name'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='locality',
            unique_together={('name', 'postal_code', 'state')},
        ),
    ]
