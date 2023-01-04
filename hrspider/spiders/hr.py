import scrapy
import json
from hrspider.items import HrspiderItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['hr.tencent.com', 'careers.tencent.com']
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        # 当前页返回招聘信息
        job_list = json.loads(response.text)['Data']['Posts']
        # 总招聘岗位数
        job_counts = json.loads(response.text)['Data']['Count']
        # 多个页面
        for job_count in range(2,job_counts//10+2):
            next_page = f'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={job_count}&pageSize=10&language=zh-cn&area=cn'
            yield scrapy.Request(next_page,callback=self.parse)
        for job in job_list:
            item = HrspiderItem()
            for key in job.keys():
                item[key] = job[key]
            # 工作详情请求
            yield scrapy.Request(
                f"https://careers.tencent.com/tencentcareer/api/post/ByPostId?postId={job['PostId']}&language=zh-cn",
                callback=self.parse_detail, meta={"item": item})

    def parse_detail(self, response):
        item = response.meta["item"]
        item['Requirement'] = json.loads(response.text)['Data']['Requirement']
        yield item
