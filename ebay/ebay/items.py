import scrapy

class ebayKleinanzeige(scrapy.Item):
  url = scrapy.Field()
  responseCompressed = scrapy.Field()
  lengthDescription = scrapy.Field()
  extParams = scrapy.Field()
  hash = scrapy.Field()
  dateCrawled = scrapy.Field()
  kw = scrapy.Field()
  verkaeufer = scrapy.Field()
  angebotstyp = scrapy.Field()
  preis =  scrapy.Field()  
  abtest = scrapy.Field()
  fahrzeugtyp = scrapy.Field()
  erstzulassungsjahr = scrapy.Field()
  getriebe = scrapy.Field()
  leistungPS = scrapy.Field()
  modell = scrapy.Field()
  kilometerstand = scrapy.Field()
  erstzulassungsmonat = scrapy.Field()
  kraftstoffart = scrapy.Field()
  marke = scrapy.Field()
  nichtReparierterSchaden = scrapy.Field()
  erstellungsdatum = scrapy.Field()
  anzahlBilder = scrapy.Field()
  plz = scrapy.Field()
  spider = scrapy.Field()
  zuletztgesehen = scrapy.Field()
  isDeleted = scrapy.Field()
  originalUrl = scrapy.Field() # only to track the original url if it has been deleted meanwhile, will not be written to db
