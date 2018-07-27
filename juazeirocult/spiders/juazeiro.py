import scrapy


class JuazeiroSpider(scrapy.Spider):
    name = 'juazeiro'
    start_urls = ['http://www.juazeiro.ce.gov.br/']

    def parse(self, response):
        url = 'http://www.juazeiro.ce.gov.br'

        logo = response.css('div.min-width img::attr(src)').extract_first()
        nome_site = response.css('title::text').extract_first()

        yield {
            'logo': url+logo,
            'nome_site': nome_site,
        }

        for next_page in response.css('div.nt-noticia a::attr(href)'):
            yield response.follow(next_page, callback=self.detail)

    def detail(self, response):

        yield {
            'titulo': response.css('header.total-min-width h2::text').extract_first(),
            'imagem': response.css('article figure.img-t1 img::attr(src)').extract_first(),
            'texto': response.css('article.texto p').extract(),
            'Descricao': response.css('article.texto p').extract_first(),
            'data': response.css('header.total-min-width h2 small::text').extract_first(),
        }

