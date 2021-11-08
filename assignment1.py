import requests
from bs4 import BeautifulSoup


class WebScrapper(object):

    request_url = "https://github.com/vinta/awesome-python"
    parsed_urls = dict()

    def get_request_url(self):
        return self.request_url

    def get_request_object(self):
        request_url = self.get_request_url()
        try:
            response = requests.get(request_url)
            if (response.status_code in range(200, 300)):
                return response
            elif (response.status_code in range(100, 200)):
                print((response.reason))
                exit()
            elif (response.status_code in range(300, 400)):
                print((response.reason))
                exit()
            elif (response.status_code in range(400, 500)):
                print((response.reason))
                exit()
        except Exception as e:
            print(e)

    def build_parser_object(self):
        response = self.get_request_object()
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup
        except Exception as e:
            print(e)

    def make_parser(self):
        try:
            soup = self.build_parser_object()
            table = soup.find('div', attrs={'class': 'Box-body px-5 pb-5'})

            for row in table.findAll('a'):
                if len(row.text.strip()) > 0 and row['href'].startswith("http"):
                    self.parsed_urls[row.text.lower()] = row['href']
        except Exception as e:
            print(e)


if __name__ == "__main__":

    while(True):
        inp = input("Query? ")
        queries = inp.split()
        query = queries and queries[-1]

        parser = WebScrapper()

        if not parser.parsed_urls:
            parser.make_parser()

        if query and parser.parsed_urls.get(query.lower()):
            print(parser.parsed_urls.get(query.lower()))
        else:
            print("Not Found, Try Again")
