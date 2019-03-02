from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader


class Informacion(Item):
    Informacion = Field()
    id = Field()
class StackOverFLowSpider(Spider):
    name = "Spider"
    start_urls =['https://www.wikipedia.org/']
    def parse(self,response):
        sel = Selector(response)
        Informacionn = sel.xpath('//div[@id ="mw-content-text"]/p')
        element in enumerate (Informacionn):
        item.ItemLoader(Informacion(),elem )
        item.add_xpath('informacion', './//a/text()')
        