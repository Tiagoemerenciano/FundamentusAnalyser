# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StockItem(Item):
    papel = Field()
    cotacao = Field()
    pl = Field()
    pvp = Field()
    psr = Field()
    dy = Field()
    pativo = Field()
    pcapgiro = Field()
    pebit = Field()
    pativ_circ_liq = Field()
    evebit = Field()
    evebitda = Field()
    mrg_ebit = Field()
    mrg_liq = Field()
    liq_corr = Field()
    roic = Field()
    roe = Field()
    liq_dois_meses = Field()
    patrim_liq = Field()
    div_brut_patrim = Field()
    cresc_rec_cinco_anos = Field()
