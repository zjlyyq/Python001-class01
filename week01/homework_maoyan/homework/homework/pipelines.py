# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd
class HomeworkPipeline:
    def process_item(self, item, spider):
        movietable = pd.DataFrame(data = item)
        # windows需要使用gbk字符集
        movietable.to_csv('./maoyan_homework.csv', encoding='utf8', index=False, header=False)
        return item
