# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.


import re
import json
import requests
import pandas as pd
from io import StringIO
import xml.etree.ElementTree as ET

headers = {
    'User-Agent': 'Paolo Barbone paolo.n.barbone@gmail.com'
}

class ExtractionError(Exception):
    pass

def get_forms_xml(cik_number):
    '''Function to get XML content for a specific CIK number'''
    index_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik_number}&type=13f-hr&dateb=&owner=exclude&output=atom"

    response = requests.get(index_url, headers=headers)
    try:
        #print the first 1000 characters of the response
        print(response.content[:100])
        return ET.fromstring(response.content)
    except ET.ParseError:
        raise ExtractionError(f"Could not parse XML content for CIK {cik_number}")
    
if __name__ == "__main__":
    cik_number = "0001166559"
    xml_content = get_forms_xml(cik_number)