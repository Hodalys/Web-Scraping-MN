# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class InformacionItem(scrapy.Item):
    titulo = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    caracteristicas = scrapy.Field()
    opiniones = scrapy.Field()
    ventas_producto = scrapy.Field()

    # Información de la tienda o vendedor
    vendedor_url = scrapy.Field()
    tipo_vendedor = scrapy.Field()
    ventas_vendedor = scrapy.Field()
