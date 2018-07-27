
from django.db import models


class New(models.Model):
    channels = models.ForeignKey('Channel', on_delete=models.CASCADE)
    titulo = models.CharField('Titulo', max_length=255, null=True, blank=True)
    descricao = models.TextField('Descrição', null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=255, null=True, blank=True)
    data = models.DateTimeField('Data',  auto_now_add=False, blank=False, null=True)
    imagem = models.ImageField(upload_to='media', null=True, blank=True)
    slug = models.SlugField('Slug', max_length=255)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return self.slug


class Channel(models.Model):
    imagem = models.ImageField(upload_to='media')
    nome = models.CharField('Nome da empresa', max_length=255)
    slug = models.SlugField('Slug', max_length=255)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Channel'
        verbose_name_plural = 'Channels'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return self.slug


class Sugestao(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    mensagem = models.TextField()

    class Meta:
        ordering = ['nome']
        verbose_name = 'Sugestão'
        verbose_name_plural = 'Sugestões'

    def __str__(self):
        return self.nome
