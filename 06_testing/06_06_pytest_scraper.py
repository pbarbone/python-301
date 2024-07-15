# Install `pytest` in a virtual environment and rewrite the test suite
# for your web scraper using `pytest` instead of `unittest`.

import pytest

from web_scraping import get_forms_xml

def test_get_forms_xml():
    cik_number = "1061165"
    xml_content = get_forms_xml(cik_number)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    company_name = xml_content.find('atom:company-info/atom:conformed-name', namespace).text
    assert company_name is not None
    assert company_name == "LONE PINE CAPITAL LLC"