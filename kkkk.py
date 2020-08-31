# Use the Request library
import requests
# Set the target webpage
url = 'http://172.18.58.238/headers.php'
r = requests.get(url)

print(r.text)

# This will get the status code
print("Status code:")
print("\t *", r.status_code)

# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an external site
url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)

--------------------------------------------------------------------------------------------------------------------------------
import json
import scrapy

class NewSpider(scrapy.Spider):
       name = "new_spider"
       start_urls = ['http://172.18.58.238/snow/']
       def parse(self, response):
                    css_selector = 'img'
                    for x in response.css(css_selector):
                                  newsel = '@src'
                                  yield {
                                        'Image Link': x.xpath(newsel).extract_first()
                                  }



            # To recurse next page
                    Page_selector = '.next a ::attr(href)'
                    next_page = response.css(Page_selector).extract_first()
                    if next_page:
                                 yield scrapy.Request(
                                        response.urljoin(next_page),
                                        callback=self.parse
                                 )
----------------------------------------------------------------------------------------------------------------------------------
[
{"image Link": "img/logo.svg"},
{"image Link": "img/logo.svg"},
{"image Link": "img/iphone.png"},
{"image Link": "img/press-01.jpg"},
{"image Link": "img/press-02.jpg"}
]
