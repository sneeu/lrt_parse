import re
import json

from pyquery import PyQuery


def main():
    stops = []
    xml = file('22.xml').read()
    xml = xml.replace(' xmlns=', ' xmlnamespace=')

    doc = PyQuery(xml)

    for stop in doc('point'):
        x = stop.find('x').text
        y = stop.find('y').text
        # name = re.sub('\s+', ' ', stop.find('nom').text)
        chainage = stop.find('num_chainage').text.lstrip()
        stops.append({'x': x, 'y': y, 'chainage': chainage})

    print json.dumps(stops)

if __name__ == '__main__':
    main()
