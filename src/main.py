from src.crawler.CrawlerInterface import CrawlerInterface
from src.crawler.naver.LocalNaverJsonParser import LocalNaverJsonParser
from src.embedd.EmbeddingInteface import EmbeddingInterface
from src.embedd.openai.OpenAIClient import OpenAIClient
from src.storage.StorageInterface import StorageInterface
from src.storage.qdrant.QdrantClient import QdrantClientStorage


def main():
    crawl: CrawlerInterface = LocalNaverJsonParser()
    embedClient: EmbeddingInterface = OpenAIClient()
    storageClient: StorageInterface = QdrantClientStorage(embedding_client=embedClient)
    
    result_datas = crawl.crawl()
    
    # already studied data
    for data in result_datas:
        embedded = embedClient.embed(data)
        storageClient.save(data=embedded)
    
    result = storageClient.query(
        "모바일 페메 연동관련글 가져와줘"
    )
    
    print(result)


if __name__ == '__main__':
    main()