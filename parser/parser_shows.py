import aiohttp
import asyncio
from lxml import etree
import xml.etree.ElementTree as ET

URL='https://soft.silverscreen.by:8443/wssite/webapi/xml?mode=showtimes'


async def parse_shows():
    async with aiohttp.ClientSession() as session:
        response = await session.get(URL)
        if response.status == 200:
            print(response.status)
            xml = await response.text()
            parser = etree.XMLParser(recover=True)
            tree = ET.fromstring(xml, parser=parser)
            for elem in tree[0]:
                for index, subelem in enumerate(elem):
                    print(index, subelem.tag, subelem.text)

# 0 ID 196087
# 1 dtAccounting None
# 2 dttmShowStart 2023-6-01T21:20:00
# 3 dttmShowStartUTC None
# 4 dttmShowEnd None
# 5 dttmShowEndUTC None
# 6 ShowSalesStartTime None
# 7 ShowSalesStartTimeUTC None
# 8 ShowSalesEndTime None
# 9 ShowSalesEndTimeUTC None
# 10 ShowReservationStartTime None
# 11 ShowReservationStartTimeUTC None
# 12 ShowReservationEndTime None
# 13 ShowReservationEndTimeUTC None
# 14 EventID 2791
# 15 Title  Стражи Галактики. Часть 3
# 16 OriginalTitle  Стражи Галактики. Часть 3
# 17 ProductionYear 2023
# 18 LengthInMinutes 155
# 19 dtLocalRelease 2023-5-06T00:00:00
# 20 Rating зрителям, достигшим 12 лет
# 21 RatingLabel 12+
# 22 RatingImageUrl None
# 23 EventType None
# 24 Genres комедия, боевик, фантастика
# 25 TheatreID 3
# 26 TheatreAuditriumID 7
# 27 TheatreAuditriumURL None
# 28 TheatreAuditorium Зал 5 MTB Kids by Visa
# 29 Theatre mooon в ТРЦ Dana Mall
# 30 TheatreAndAuditorium mooon в ТРЦ Dana Mall, Зал 5 MTB Kids by Visa
# 31 PresentationMethodAndLanguage None
# 32 EventSeries None
# 33 ShowURL https://silverscreen.by/afisha/#times=strazhi-galaktiki-chast-3-2791=196087
# 34 PresentationMethod 2D
# 35 EventURL https://silverscreen.by/afisha/strazhi-galaktiki-chast-3-2791
# 36 Images None
# 37 ContentDescriptors None
# 38 hav_tickets true
# 39 min_price 0.1
# 40 max_price 26


if __name__=="__main__":
    loop = asyncio.new_event_loop() # создаём новый асинхронный цикл
    loop.create_task(parse_shows()) # добавляем в него нашу функцию
    loop.run_forever()