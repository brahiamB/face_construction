# Generated by Django 3.0.5 on 2020-07-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='job',
            field=models.CharField(choices=[('Excavation', 'Excavation'), ('Demolition', 'Demolition'), ('Snow removal', 'Snow removal'), ('Asphalt paving', 'Asphalt paving'), ('Concrete pavement', 'Concret pavement'), ('Commercila Pavement', 'Commercial Pavement')], max_length=256),
        ),
    ]