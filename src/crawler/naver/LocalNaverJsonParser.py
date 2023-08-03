import json

from typing import List
from src.crawler.CrawlerInterface import CralwerInterface
from src.crawler.SourceData import SourceData


class LocalNaverJsonParser(CralwerInterface):
    
    def __init__(self):
        pass
    
    def crawl(self) -> List[SourceData]:
        result_arr = []
        with open('data_set/kr/naver_qna.json', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            for data in json_data:
                result_arr.append(
                    SourceData(
                        text=f"질문: {data['질문']}, 답변: {data['답변']}",
                        ref=data["ref"],
                    )
                )
        return result_arr
    
    
if __name__ == '__main__':
    crawl = LocalNaverJsonParser()
    crawl.crawl()