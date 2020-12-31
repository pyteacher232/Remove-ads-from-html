from lxml.etree import tostring
import lxml.html
import requests

# take AdRemover code from here:
# https://github.com/buriy/python-readability/issues/43#issuecomment-321174825
from adremover import AdRemover


rule_files = ["1.txt", "ruadlist+easylist.txt"]
remover = AdRemover(*rule_files)

html = open("page.html", "r", encoding='utf-8').read()
document = lxml.html.document_fromstring(html)
remover.remove_ads(document)
clean_html = tostring(document).decode("utf-8")
print(clean_html)