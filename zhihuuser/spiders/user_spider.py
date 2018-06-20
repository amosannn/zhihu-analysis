# -*- coding: utf-8 -*-
import json
from zhihuuser.items import ZhihuItem
from scrapy import Request, Spider

class ZhihuuserSpider(Spider):
    name = 'zhihuuser'
    allowed_domains = ["www.zhihu.com"]
    start_urls = ["https://www.zhihu.com/"]
    start_user = "lin-jia-sheng-96"
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset={offset}&limit=20'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_include = 'locations,voteup_count,thanked_count,follower_count,following_count,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,question_count,commercial_question_count,favorite_count,favorited_count,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,description'
    #可选内容：locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics
    
    def start_requests(self):
        yield Request(self.followees_url.format(user=self.start_user, offset=0), callback=self.parse_fo)
        yield Request(self.user_url.format(user=self.start_user, include=self.user_include), callback=self.parse_user)

    def parse_user(self, response):
        result = json.loads(response.text)
        print(result)
        item = ZhihuItem()
        item['user_name'] = result['name']
        item['sex'] = result['gender']  # gender为1是男，0是女，-1是未设置
        item['user_sign'] = result['headline']
        item['user_avatar'] = result['avatar_url_template'].format(size='xl')
        item['user_url'] = 'https://www.zhihu.com/people/' + result['url_token']
        item['locations'] = result['locations'][0]['name'] if len(result['locations']) else ''
        item['voteup_count'] = result['voteup_count'] 
        item['thanked_count'] = result['thanked_count'] if result['thanked_count'] else 0
        item['follower_count'] = result['follower_count'] if result['follower_count'] else 0
        item['following_count'] = result['following_count'] if result['following_count'] else 0
        item['following_topic_count'] = result['following_topic_count'] if result['following_topic_count'] else 0
        item['following_question_count'] = result['following_question_count'] if result['following_question_count'] else 0
        item['following_favlists_count'] = result['following_favlists_count'] if result['following_favlists_count'] else 0
        item['following_columns_count'] = result['following_columns_count'] if result['following_columns_count'] else 0
        item['answer_count'] = result['answer_count'] if result['answer_count'] else 0
        item['articles_count'] = result['articles_count'] if result['articles_count'] else 0
        item['question_count'] = result['question_count'] if result['question_count'] else 0
        item['commercial_question_count'] = result['commercial_question_count'] if result['commercial_question_count'] else 0
        item['favorite_count'] = result['favorite_count'] if result['favorite_count'] else 0
        item['favorited_count'] = result['favorited_count'] if result['favorited_count'] else 0
        item['is_bind_sina'] = result['is_bind_sina'] if result['is_bind_sina'] else 0
        #item['sina_weibo_url'] = result['sina_weibo_url'] if result['sina_weibo_url'] else ''
        #item['sina_weibo_name'] = result['sina_weibo_name'] if result['sina_weibo_name'] else 0
        #item['show_sina_weibo'] = result['show_sina_weibo'] if result['show_sina_weibo'] else 0
        item['is_following'] = result['is_following'] if result['is_following'] else 0
        item['is_followed'] = result['is_followed'] if result['is_followed'] else 0
        item['mutual_followees_count'] = result['mutual_followees_count'] if result['mutual_followees_count'] else 0
        item['vote_to_count'] = result['vote_to_count'] if result['vote_to_count'] else 0
        item['vote_from_count'] = result['vote_from_count'] if result['vote_from_count'] else 0
        item['thank_to_count'] = result['thank_to_count'] if result['thank_to_count'] else 0
        item['thank_from_count'] = result['thank_from_count'] if result['thank_from_count'] else 0
        item['thanked_count'] = result['thanked_count'] if result['thanked_count'] else 0
        item['description'] = result['description'] if result['description'] else ''
        yield item

    def parse_fo(self, response):
        results = json.loads(response.text)
        for result in results['data']:
            yield Request(self.user_url.format(user=result['url_token'], include=self.user_include), callback=self.parse_user)
            if result['url_token'] !=self.start_user:
                # 对关注者的关注者进行遍历，爬取深度depth+=1
                yield Request(self.followees_url.format(user=result['url_token'], offset=0), callback=self.parse_fo)  
            else:
                pass

        #关注列表页是否为尾页
        if results['paging']['is_end'] is False: 
            next_url = results['paging']['next'].replace('http','https')
            yield Request(next_url,callback=self.parse_fo)
        else:
            pass