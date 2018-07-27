# Generated by Django 2.0.2 on 2018-06-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sugestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mensagem', models.TextField()),
            ],
            options={
                'verbose_name': 'Sugestão',
                'verbose_name_plural': 'Sugestões',
                'ordering': ['nome'],
            },
        ),
        migrations.AlterField(
            model_name='new',
            name='data',
            field=models.DateTimeField(null=True, verbose_name='Data'),
        ),
    ]
