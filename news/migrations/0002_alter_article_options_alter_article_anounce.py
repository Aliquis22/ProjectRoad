# Generated by Django 4.2.3 on 2023-07-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='article',
            name='anounce',
            field=models.CharField(max_length=300, verbose_name='Анонс'),
        ),
    ]
