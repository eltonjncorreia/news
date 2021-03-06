# Generated by Django 2.0.2 on 2018-07-27 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='media')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da empresa')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titulo')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('texto', models.TextField(blank=True, null=True)),
                ('autor', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.DateTimeField(null=True, verbose_name='Data')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('channels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Channel')),
            ],
            options={
                'verbose_name': 'New',
                'verbose_name_plural': 'News',
            },
        ),
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
    ]
