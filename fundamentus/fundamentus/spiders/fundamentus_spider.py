import scrapy
import logging
from fundamentus.items import StockItem
from scrapy.loader import ItemLoader

class FundamentusSpider(scrapy.Spider):
    name = 'fundamentus'

    def start_requests(self):
        param_negociada = 'ON'
        param_ordem = '1'
        yield scrapy.FormRequest(
            url='http://www.fundamentus.com.br/resultado.php?negociada=ON&ordem=1',
            callback=self.parse,
            headers={
                'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
                'Accept': 'text/html, text/plain, text/css, text/sgml, */*;q=0.01'
            },
            formdata=dict(negociada=param_negociada, ordem=param_ordem)
        )

    def parse(self, response):      
      stock_model = StockItem()

      data_table = response.xpath('//*[@id="resultado"]/tbody/tr')

      for index_line, data_line in enumerate(data_table):
          data_line = response.xpath(
              '//*[@id="resultado"]/tbody/tr[{0}]'.format(index_line+1))

          stock_model['papel'] = data_line.xpath('.//td[1]/span/a/text()').get()
          stock_model['cotacao'] = data_line.xpath('.//td[2]/text()').get()
          stock_model['pl'] = data_line.xpath('.//td[3]/text()').get()
          stock_model['pvp'] = data_line.xpath('.//td[4]/text()').get()
          stock_model['psr'] = data_line.xpath('.//td[5]/text()').get()
          stock_model['dy'] = data_line.xpath('.//td[6]/text()').get()
          stock_model['pativo'] = data_line.xpath('.//td[7]/text()').get()
          stock_model['pcapgiro'] = data_line.xpath('.//td[8]/text()').get()
          stock_model['pebit'] = data_line.xpath('.//td[9]/text()').get()
          stock_model['pativ_circ_liq'] = data_line.xpath('.//td[10]/text()').get()
          stock_model['evebit'] = data_line.xpath('.//td[11]/text()').get()
          stock_model['evebitda'] = data_line.xpath('.//td[12]/text()').get()
          stock_model['mrg_ebit'] = data_line.xpath('.//td[13]/text()').get()
          stock_model['mrg_liq'] = data_line.xpath('.//td[14]/text()').get()
          stock_model['liq_corr'] = data_line.xpath('.//td[15]/text()').get()
          stock_model['roic'] = data_line.xpath('.//td[16]/text()').get()
          stock_model['roe'] = data_line.xpath('.//td[17]/text()').get()
          stock_model['liq_dois_meses'] = data_line.xpath('.//td[18]/text()').get()
          stock_model['patrim_liq'] = data_line.xpath('.//td[19]/text()').get()
          stock_model['div_brut_patrim'] = data_line.xpath('.//td[20]/text()').get()
          stock_model['cresc_rec_cinco_anos'] = data_line.xpath('.//td[21]/text()').get()
          yield stock_model