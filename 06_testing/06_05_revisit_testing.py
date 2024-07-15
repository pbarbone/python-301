# Revisit one of the previous lab exercises that were challenging for you.
# Write a test suite that checks for the correct functionality of the code.
# Then try to refactor your solution, maybe you can make the code more
# concise or more elegant? Keep checking whether you broke the functionality
# by repeatedly running your test suite against your changes.


from unittest import TestCase
from web_scraping import get_forms_xml

class TestWebScraper(TestCase):
    def test_get_forms_xml(self):
        cik_number = "1061165"
        xml_content = get_forms_xml(cik_number)
        namespace = {"atom": "http://www.w3.org/2005/Atom"}
        company_name = xml_content.find('atom:company-info/atom:conformed-name', namespace).text
        self.assertNotEqual(company_name, None)
        self.assertEqual(company_name, "LONE PINE CAPITAL LLC")