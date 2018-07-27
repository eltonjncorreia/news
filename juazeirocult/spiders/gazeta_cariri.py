import scrapy


class GazetaSpider(scrapy.Spider):
    name = 'gazeta'
    start_urls = ['http://www.gazetadocariri.com/']

    def parse(self, response):
        logo = response.css('div.header-logo img::attr(src)').extract_first()
        nome_site = response.css('div.header-logo img::attr(alt)').extract_first()

        yield {
            'logo': logo,
            'nome_site': nome_site,

        }

        for div in response.css('div.blog-posts div.post-outer'):
            item = div.css('div.post h2 a::attr(src)').extract_first()

            yield scrapy.Request('{}'.format(item), callback=self.detail)

    def detail(self, response):
        yield {
            'imagem': response.css('img::attr(src)').extract_first(),
            # 'titulo': response.css('div.esquerda div.fonte_termo::text').extract_first(),
            # 'autor': response.css('div.esquerda  div.fonte_autor b::text').extract_first(),
            # 'Descricao': response.css('div.esquerda h1::text').extract_first(),
            # 'data': response.css('div.esquerda div.fonte_dh b::text').extract_first(),
            # 'texto': response.css('div.esquerda div.fonte_not p::text').extract(),
        }

