# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='root',
        charset='utf8',
        use_unicode=False
    )
    return conn

class ZhihuPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()  # 写入数据库
        cursor = dbObject.cursor()
        #sql = "insert into scrapy.zhihu_user(user_name,sex,user_sign,user_avatar,user_url,locations,voteup_count,thanked_count,follower_count,following_count,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,question_count,commercial_question_count,favorite_count,favorited_count,is_bind_sina,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #param = (item['user_name'],item['sex'],item['user_sign'],item['user_avatar'],item['user_url'],item['locations'],item['voteup_count'],item['thanked_count'],item['follower_count'],item['following_count'],item['following_topic_count'],item['following_question_count'],item['following_favlists_count'],item['following_columns_count'],item['answer_count'],item['articles_count'],item['question_count'],item['commercial_question_count'],item['favorite_count'],item['favorited_count'],item['is_bind_sina'],item['is_following'],item['is_followed'],item['mutual_followees_count'],item['vote_to_count'],item['vote_from_count'],item['thank_to_count'],item['thank_from_count'],item['description'])
        sql = "insert into scrapy.zhihu_user(user_name,sex,user_sign,user_avatar,user_url,locations,voteup_count,thanked_count,follower_count,following_count,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,question_count,commercial_question_count,favorite_count,favorited_count,is_bind_sina,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,description) values({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19},{20},{21},{22},{23},{24},{25},{26},{27},{28})"
      
        try:
            cursor.execute(sql.format("\'"+item['user_name']+"\'",item['sex'],"\'"+item['user_sign']+"\'","\'"+item['user_avatar']+"\'","\'"+item['user_url']+"\'","\'"+item['locations']+"\'",item['voteup_count'],item['thanked_count'],item['follower_count'],item['following_count'],item['following_topic_count'],item['following_question_count'],item['following_favlists_count'],item['following_columns_count'],item['answer_count'],item['articles_count'],item['question_count'],item['commercial_question_count'],item['favorite_count'],item['favorited_count'],item['is_bind_sina'],item['is_following'],item['is_followed'],item['mutual_followees_count'],item['vote_to_count'],item['vote_from_count'],item['thank_to_count'],item['thank_from_count'],"\'"+item['description']+"\'"))
            dbObject.commit()
        except Exception as e:
            print(e)
            dbObject.rollback()
        return item
