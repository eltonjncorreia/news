# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'miseria'
    start_urls = ['http://www.miseria.com.br/']

    def parse(self, response):
        url = 'http://www.miseria.com.br/'
        logo = response.css('div.logo_topo img::attr(src)').extract_first()
        nome_site = response.css('title::text').extract_first()

        yield {
            'logo': url+logo,
            'nome_site': nome_site
        }

        for div in response.css('div.bxslider div.infos'):
            item = div.css('a::attr(href)').extract_first()

            yield scrapy.Request('{}'.format(item), callback=self.detail)

    def detail(self, response):
        yield {
            'imagem': response.css('div.esquerda div.espaco_foto_capa img::attr(src)').extract_first(),
            'titulo': response.css('div.esquerda div.fonte_termo::text').extract_first(),
            'autor': response.css('div.esquerda  div.fonte_autor b::text').extract_first(),
            'Descricao': response.css('div.esquerda h1::text').extract_first(),
            'data': response.css('div.esquerda div.fonte_dh b::text').extract_first(),
            'texto': response.css('div.esquerda div.fonte_not p::text').extract(),
        }

