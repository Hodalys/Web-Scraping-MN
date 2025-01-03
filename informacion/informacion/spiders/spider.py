import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from informacion.items import InformacionItem

class InformacionSpider(CrawlSpider):
    name = 'mercado'
    item_count = 0 # opcional
    allowed_domain = ['www.mercadolibre.com.ec']
    start_url = ['https://listado.mercadolibre.com.ec/computadoras-portatiles#D[A:computadoras%20portatiles]']

    rules = {
        # Página siguiente
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//li[@class="andes-pagination__button andes-pagination__button--next"]/a'))),
        # Búsqueda en cada objeto que encuentre
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//h2[@class="poly-box poly-component__title"]')),
                            callback='parse_item', follow= False),
        
    }

    def parse_item(self,  response):
        ml_item = InformacionItem()

        #Importar los items
        #Info del producto
        ml_item['titulo'] = response.xpath('normalize-space(/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[2]/h1)').extract()
        ml_item['precio'] = response.xpath('normalize-space(/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[1]/div[1]/span/span/span[2])').extract()
        ml_item['condicion'] = response.xpath('normalize-space(/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[7]/div/div[2]/div[2]/text())').extract()
        ml_item['envio'] = response.xpath('normalize-space(/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[1])/text()').extract()
        ml_item['caracteristicas'] = response.xpath('normalize-space(/html/body/main/div[2]/div[5]/div[2]/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div[1]/div/table)').extract()
        ml_item['opiniones'] = response.xpath('normalize-space(/html/body/main/div[2]/div[5]/div[2]/div[2]/div[2]/div[5]/div/div/section/div/div[1]/div/div[1]/div[1]/p)').extract()
        ml_item['ventas_producto'] = response.xpath('/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[1]/div/div[1]/span').extract()
        
        #Info de la tienda o vendedor
        ml_item['vendedor_url'] = response.xpath('//*[@id="ui-pdp-main-container"]/div[2]/div[2]/section[2]/div/a').extract()
        ml_item['tipo_vendedor'] = response.xpath('/html/body/main/div[2]/div[5]/div[2]/div[1]/div/div[1]/div/div[7]/div/div/div[1]/div/button/span[2]').extract()
        ml_item['ventas_vendedor'] = response.xpath('/html/body/div[4]/div/div/div[2]/div[2]/div/div/div/ul/li[1]/strong/text()').extract()
        self.item_count += 1
        if self.item_count > 20:
            raise CloseSpider('item_exceeded')
        yield ml_item
        
        