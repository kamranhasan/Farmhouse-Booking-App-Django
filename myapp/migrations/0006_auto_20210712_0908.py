# Generated by Django 3.1.6 on 2021-07-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210509_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Name',
            new_name='Your_Name',
        ),
        migrations.AddField(
            model_name='book',
            name='farmhouse_Name',
            field=models.CharField(choices=[('Maple', 'Maple')], default='Maple', max_length=100),
        ),
        migrations.AddField(
            model_name='check',
            name='farmhouse_Name',
            field=models.CharField(choices=[('Maple', 'Maple')], default='Maple', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='Day_or_Night',
            field=models.CharField(choices=[('Day', 'Day')], max_length=100),
        ),
    ]
