import xmltodict

with open('./data/64_72hr_CH.xml', encoding='UTF-8') as fd:
    doc = dict(xmltodict.parse(fd.read()))

sect_with_tempers = doc["cwbopendata"]["dataset"]["locations"]["location"]

for sect_with_temper in sect_with_tempers:
    if sect_with_temper['locationName'] == '鹽埕區':
        for weatherElement in sect_with_temper['weatherElement']:
            if weatherElement['description'] == '溫度':
                for time in weatherElement['time']:
                    print(time['dataTime'], time['elementValue']['value'])
