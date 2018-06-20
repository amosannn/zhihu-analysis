# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_name = scrapy.Field()
    sex  = scrapy.Field()
    user_sign = scrapy.Field()
    user_url = scrapy.Field()
    user_avatar = scrapy.Field()
    locations = scrapy.Field()
    voteup_count = scrapy.Field()
    thanked_Count = scrapy.Field()
    follower_count = scrapy.Field()
    following_count = scrapy.Field()
    following_topic_count = scrapy.Field()
    following_question_count = scrapy.Field()
    following_favlists_count = scrapy.Field()
    following_columns_count = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    question_count = scrapy.Field()
    commercial_question_count = scrapy.Field()
    favorite_count = scrapy.Field()
    favorited_count = scrapy.Field()
    is_bind_sina = scrapy.Field()
    sina_weibo_url = scrapy.Field()
    sina_weibo_name = scrapy.Field()
    show_sina_weibo = scrapy.Field()
    is_following = scrapy.Field()
    is_followed = scrapy.Field()
    mutual_followees_count = scrapy.Field()
    vote_to_count = scrapy.Field()
    vote_from_count = scrapy.Field()
    thank_to_count = scrapy.Field()
    thank_from_count = scrapy.Field()
    thanked_count = scrapy.Field()
    description = scrapy.Field()
    pass
