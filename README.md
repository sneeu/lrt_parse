# lrt_parse

A few bits for parsing the route information from [mybustracker.co.uk](http://mybustracker.co.uk/).

    pip install pyquery
    curl http://mybustracker.co.uk/getServicePoints.php?serviceMnemo=22 > 22.xml
    python parse.py > 22.json
    open index.html
