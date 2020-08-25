print('Hello')

#First HTTP Server
import socket;
#Define the host as a tuple
HOST, PORT = "", 8080;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1);
s.bind((HOST,PORT));
s.listen(True);

print("Serving HTTP on port %s...." %PORT);

while True:
    client_connection, client_address = s.accept();
    request = client_connection.recv(1024); #Buffer Size
    print(request.decode("utf-8")); #Display the HTTP request
    #Define the Web response message
    http_reponse = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Welcome This is my first webpage, GREAT!
"""
    client_connection.sendall(bytes(http_reponse, "utf-8"));
    client_connection.close();
# Use the Request library
import requests
# Set the target webpage
url = 'http://www.wikipedia.org’
r = requests.get(url)
# This will get the full page
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
    'User-Agent' : ‘Iphone 8’
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
import scrapy  class NewSpider(scrapy.Spider):
      name = "new_spider"
      start_urls = ['http://192.168.1.1/sets/1']
class NewSpider(scrapy.Spider):
 	name = "new_spider"
 	start_urls = ['http://192.168.1.1/index.html']  	def parse(self, response):
 	 	css_selector = 'img'  	 	for x in response.css(css_selector):
 	 	 	newsel = '@src'
 	 	 	yield {
 	 	 	        'Image Link': x.xpath(newsel).extract_first(),
 	 	 	}


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://192.168.1.1/index.html']

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }

            # To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(  	 	 	 response.urljoin(next_page),
                                                 callback=self.parse
                                                 )

