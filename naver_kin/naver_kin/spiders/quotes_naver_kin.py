import scrapy

class exampleSpider(scrapy.Spider):
    name = 'kinspider'
    category = '2'
    kin_urls = 'http://kin.naver.com/qna/list.nhn?dirId=' + category
    start_urls = [kin_urls]
    
    def parse(self, response):
        for item in response.css('td.title a'):
            yield response.follow(item, self.parse_doc)

        # for next_page in response.css('div.paginate > a'):
        #     yield response.follow(next_page, self.parse)

    def parse_doc(self, response):
        result = []
        docId = response.request.url.split("docId=")[-1]
        title = response.css('div.title::text').extract_first().strip().encode('utf8')
        question_contents = response.css('div.c-heading__content ::text').extract()
        question = "\n\n".encode('utf8')
        for q in question_contents:
            question += q.strip().encode('utf8')
            question += "\n".encode('utf8')
            
        return {
            'ref': response.request.url,
            'title': title.decode('utf8'),
            'question': question.decode('utf8'),
        }

if __name__ == '__main__':
    pass