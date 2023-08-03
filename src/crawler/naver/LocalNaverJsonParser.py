import jsonlines

from typing import List
from src.crawler.CrawlerInterface import CrawlerInterface
from src.crawler.SourceData import SourceData


class LocalNaverJsonParser(CrawlerInterface):
    
    def __init__(self):
        pass
    
    def crawl(self) -> List[SourceData]:
        result_arr = []
        with jsonlines.open('data_set/kr/kin.jsonl') as json_file:
            for data in json_file.iter():
                result_arr.append(
                    SourceData(
                        text=f"제목: {data['title']} 질문: {data['question']}",
                        ref=data["ref"],
                    )
                )
        return result_arr
    
    
if __name__ == '__main__':
    crawl = LocalNaverJsonParser()
    crawl.crawl()