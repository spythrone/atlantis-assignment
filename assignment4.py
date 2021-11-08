import requests
from requests.models import Response
from bs4 import BeautifulSoup


class WikiFinder(object):

    def __init__(self, url):
        self.request_url = url
        self.paragraphs = []
        self.three_letter_words = 0
        self.four_letter_words = 0
        self.five_letter_words = 0

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
            table = soup.find('div', attrs={'class': 'mw-body'})

            for row in table.findAll('p'):
                if len(row.text.strip()) > 0:
                    self.paragraphs.append(row.text.strip())
            for para in self.paragraphs:
                words = para.split()
                for word in words:
                    if len(word) == 3:
                        self.three_letter_words = self.three_letter_words+1
                    if len(word) == 4:
                        self.four_letter_words = self.four_letter_words+1
                    if len(word) == 5:
                        self.five_letter_words = self.five_letter_words+1

        except Exception as e:
            print(e)

    def get_details(self):
        print("3-letter words: {} / paragraph".format(int(self.three_letter_words/len(self.paragraphs))))
        print("4-letter words: {} / paragraph".format(int(self.four_letter_words/len(self.paragraphs))))
        print("5-letter words: {} / paragraph".format(int(self.five_letter_words/len(self.paragraphs))))


if __name__ == "__main__":

    while(True):
        inp = input("Enter wikipedia page? ")
        parser = WikiFinder(inp)
        parser.make_parser()
        parser.get_details()
