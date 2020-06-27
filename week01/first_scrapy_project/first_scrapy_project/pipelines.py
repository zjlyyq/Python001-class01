# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class FirstScrapyProjectPipeline:
    # def process_item(self, item, spider):
    #     # movieinfo = pd.DataFrame(data=item)
    #     # movieinfo.to_csv('./movies.csv', encoding='utf8', index=False, header=False)
    #     return item

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        content = item['content']
        output = f'|{title}|\t|{link}|\t|{content}|\n\n'
        with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
            
        return item
    
