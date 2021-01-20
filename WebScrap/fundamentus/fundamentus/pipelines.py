# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import psycopg2

from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
import logging

logger = logging.getLogger('pipeline')

class FundamentusPostgrePipeline(object):
  def open_spider(self, spider):
    hostname = 'host.docker.internal'
    username = 'postgres'
    password = 'postgres'
    database = 'postgres'
    port = 5432
    self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
    self.cursor = self.connection.cursor()

  def close_spider(self, spider):
    self.cursor.close()
    self.connection.close()

  def process_item(self, item, spider):
    try:
      self.cursor.execute("""
      INSERT INTO fundamentos.papeis(codigo) 
      VALUES ('{0}') 
      ON CONFLICT (codigo) DO NOTHING""".format(item['papel']))
      
      self.cursor.execute("""
      INSERT INTO fundamentos.fundamentos 
      (
        id, 
        preco_por_lucro, 
        preco_por_valorpatrimonial, 
        psr, 
        dividend_yield, 
        preco_por_ativos, 
        preco_por_capitaldegiro, 
        preco_por_ativocirculanteliquido, 
        preco_por_ebit, 
        ev_por_ebit, 
        ev_por_ebitda, 
        margem_ebit, 
        margem_liquida, 
        liquidez_corrente, 
        roic, 
        roe, 
        liquidez_dois_meses, 
        divida_bruta_por_patrimonio, 
        crescimento_receita_cinco_anos, 
        papel, 
        data_alteracao, 
        patrimonio_liquido 
      ) VALUES (gen_random_uuid(), {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, '{18}', CURRENT_TIMESTAMP, {19}) ON CONFLICT (papel) DO 
        UPDATE SET 
          preco_por_lucro = {0},
          preco_por_valorpatrimonial = {1},
          psr = {2},
          dividend_yield = {3},
          preco_por_ativos = {4},
          preco_por_capitaldegiro = {5},
          preco_por_ativocirculanteliquido = {6},
          preco_por_ebit = {7},
          ev_por_ebit = {8},
          ev_por_ebitda = {9},
          margem_ebit = {10},
          margem_liquida = {11},
          liquidez_corrente = {12},
          roic = {13},
          roe = {14},
          liquidez_dois_meses = {15},
          divida_bruta_por_patrimonio = {16},
          crescimento_receita_cinco_anos = {17},
          data_alteracao = CURRENT_TIMESTAMP,
          patrimonio_liquido = {19}
        """.format(
        item['pl'].replace('.', '').replace(',', '.'), 
        item['pvp'].replace('.', '').replace(',', '.'),
        item['psr'].replace('.', '').replace(',', '.'), 
        item['dy'].replace('%', '').replace('.', '').replace(',', '.'), 
        item['pativo'].replace('.', '').replace(',', '.'), 
        item['pcapgiro'].replace('.', '').replace(',', '.'), 
        item['pativ_circ_liq'].replace('.', '').replace(',', '.'), 
        item['pebit'].replace('.', '').replace(',', '.'), 
        item['evebit'].replace('.', '').replace(',', '.'), 
        item['evebitda'].replace('.', '').replace(',', '.'), 
        item['mrg_ebit'].replace('%', '').replace('.', '').replace(',', '.'), 
        item['mrg_liq'].replace('%', '').replace('.', '').replace(',', '.'), 
        item['liq_corr'].replace('.', '').replace(',', '.'), 
        item['roic'].replace('%', '').replace('.', '').replace(',', '.'), 
        item['roe'].replace('%', '').replace('.', '').replace(',', '.'), 
        item['liq_dois_meses'].replace('.', '').replace(',', '.'), 
        item['div_brut_patrim'].replace('.', '').replace(',', '.'), 
        item['cresc_rec_cinco_anos'].replace('%', '').replace('.', '').replace(',', '.'), 
        item['papel'].replace('.', '').replace(',', '.'), 
        item['patrim_liq'].replace('.', '').replace(',', '.')
      ))
      self.connection.commit()
    except psycopg2.DatabaseError as error:
      logger.error(error)
      self.connection.rollback()
      pass
    
    return item