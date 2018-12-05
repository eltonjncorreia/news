import os
import json
from dateutil import parser

from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render, resolve_url as r

from website.core.forms import SugestaoModelForm
from .models import Channel, New
from website.settings import BASE_DIR

import re
from unicodedata import normalize


def home(request):
    # create_news_channel('website/news_json/miseria.json')
    create_news_channel('website/news_json/juazeiro.json')
    todos_channels = Channel.objects.all()
    if request.method == 'POST':
        form = SugestaoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso. Agradecemos a sugestão.')
            return HttpResponseRedirect(r('news:home'))
    else:
        form = SugestaoModelForm()
    return render(request, 'core/index.html', {'texto': todos_channels, 'form': form})


def page_ajuda(request):
    return render(request, 'core/ajudeosite.html')


def todos(request, slug):
    if slug == 'prefeitura-municipal-de-juazeiro-do-norte':
        create_news('website/news_json/juazeiro.json', slug)

    elif slug == 'site-miseria-aconteceu-ta-no-miseria':
        create_news('website/news_json/miseria.json', slug)

    todos_news_channel = New.objects.filter(channels__slug=slug).order_by('-data')[:15]
    channel = Channel.objects.get(slug=slug)

    return render(request, 'core/todos.html', {'texto': todos_news_channel, 'channel': channel})


def detail(request, slug):
    new = New.objects.get(slug=slug)
    return render(request, 'core/page_news.html', {'new': new})


def open_json(caminho):
    js = open(os.path.join(BASE_DIR, "{}".format(caminho)))
    aq_lido = js.read()
    texto = json.loads(aq_lido)
    return texto


def create_news_channel(caminho):
    nome_site = open_json(caminho)[0]['nome_site']

    channel = Channel.objects.filter(nome__contains=nome_site)

    if not channel:
        Channel.objects.create(nome=nome_site,
                               imagem=open_json(caminho)[0]['logo'],
                               slug=create_slug(nome_site))


def create_news(caminho, slug):
    channel = Channel.objects.get(slug=slug)

    for valor in open_json(caminho)[1:]:
            titulo = New.objects.filter(titulo__contains=valor.get('titulo'))

            if not titulo:
                slug = valor.get('titulo')
                data = valor.get('data')
                dt = data_format(data)
                texto = "".join(valor.get('texto'))

                New.objects.create(titulo=valor.get('titulo'),
                                   descricao=valor.get('Descricao'),
                                   texto=texto,
                                   data=dt,
                                   autor=valor.get('autor'),
                                   imagem=valor.get('imagem'),
                                   slug=create_slug(slug),
                                   channels=channel)


def data_format(data=None):
    nova_dt = data.replace(' de ', '/')
    lista_dt = nova_dt.split('/')
    numero_mes = mes(lista_dt[1])
    lista_dt.pop(1)
    lista_dt.insert(1, numero_mes)
    data = "/".join(lista_dt)
    data = parser.parse(data, dayfirst=True)
    return data


def create_slug(texto):
    expressao = re.compile(r'\W+')
    texto_sem_acentos = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto_sub = expressao.sub('-', texto_sem_acentos).lower()
    return texto_sub


def mes(mes):

    if mes == 'janeiro':
        return '01'
    elif mes == 'fevereiro':
        return '02'
    elif mes == 'marco':
        return '03'
    elif mes == 'abril':
        return '04'
    elif mes == 'maio':
        return '05'
    elif mes == 'junho':
        return '06'
    elif mes == 'julho':
        return '07'
    elif mes == 'agosto':
        return '08'
    elif mes == 'setembro':
        return '09'
    elif mes == 'outubro':
        return '10'
    elif mes == 'novembro':
        return '11'
    elif mes == 'dezembro':
        return '12'
    else:
        return mes

