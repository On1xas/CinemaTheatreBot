import aiohttp
import asyncio
from lxml import etree
import xml.etree.ElementTree as ET

URL='https://soft.silverscreen.by:8443/wssite/webapi/xml?mode=events'


async def parse_shows():
    async with aiohttp.ClientSession() as session:
        response = await session.get(URL)
        if response.status == 200:
            print(response.status)
            xml = await response.text()
            parser = etree.XMLParser(recover=True)
            tree = ET.fromstring(xml, parser=parser)
            for elem in tree:
                for index, subelem in enumerate(elem):
                    print(index, subelem.tag, subelem.text)

# 0 ID 2839
# 1 Title  Питомец юрского периода. Утраченная тайна
# 2 OriginalTitle  Питомец юрского периода. Утраченная тайна
# 3 ProductionYear 2023
# 4 LengthInMinutes 90
# 5 dtLocalRelease 2023-6-01T00:00:00
# 6 Rating зрителям, достигшим 12 лет
# 7 RatingLabel 12+
# 8 RatingImageUrl None
# 9 LocalDistributorName None
# 10 GlobalDistributorName None
# 11 ProductionCompanies None
# 12 EventType None
# 13 Genres семейный, приключения
# 14 ShortSynopsis Венди обычный тинейджер, но приключения ждут её каждый день, ведь она — хранитель тайных врат в затерянный мир динозавров. Однажды детёныш динозавра решает остаться в нашем времени, но таинственная группа преступников начинает за ним охоту и теперь только Венди сможет вернуть домой питомца юрского периода.
# 15 Synopsis Венди обычный тинейджер, но приключения ждут её каждый день, ведь она — хранитель тайных врат в затерянный мир динозавров. Однажды детёныш динозавра решает остаться в нашем времени, но таинственная группа преступников начинает за ним охоту и теперь только Венди сможет вернуть домой питомца юрского периода.
# 16 EventURL https://silverscreen.by/afisha/pitomec-jurskogo-perioda-utrachennaya-tajna-2839
# 17 Images None
# 18 Cast None
# 19 Directors None
# 20 ContentDescriptors None

if __name__=="__main__":
    loop = asyncio.new_event_loop() # создаём новый асинхронный цикл
    loop.create_task(parse_shows()) # добавляем в него нашу функцию
    loop.run_forever()