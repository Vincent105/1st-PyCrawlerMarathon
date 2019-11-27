import xmltodict
with open('./data/64_72hr_CH.xml', encoding='UTF-8-sig') as fd:
    doc = dict(xmltodict.parse(fd.read()))


locations = doc["cwbopendata"]["dataset"]["locations"]["location"]

print(doc["cwbopendata"]["dataset"]["locations"]["location"])
