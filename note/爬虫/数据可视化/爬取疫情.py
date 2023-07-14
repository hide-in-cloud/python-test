import json
from bs4 import BeautifulSoup
import requests
import re
import tqdm


class CoronaVirusSpider(object):

    def __init__(self):
        self.home_url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

    def get_content_from_url(self, url):
        """获取首页html信息"""
        response = requests.get(url)
        return response.content.decode('utf-8')

    def parse_home_page(self, home_page, tag_id):
        """根据标签解析html信息"""
        soup = BeautifulSoup(home_page, "lxml")
        tag = soup.find(name='script', attrs={'id': tag_id})
        text = tag.text

        match = re.search(r'\[.+\]', text)
        json_str = match.group()

        # 把json字符串转换成python型数据
        data = json.loads(json_str)
        return data

    def parse_statistics_data(self, total_data, desc):
        corona_virus = []
        # 各国的统计数据
        for country in tqdm.tqdm(total_data, desc):
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            total_statistics_data = json.loads(statistics_data_json_str)['data']
            # 为各国数据添加国家名称
            for country_statisticsData in total_statistics_data:
                country_statisticsData['provinceName'] = country['provinceName']
                if country.get('countryShortCode'):
                    country_statisticsData['countryShortCode'] = country['countryShortCode']
            corona_virus.extend(total_statistics_data)
        return corona_virus

    def load(self, path):
        """根据路径加载数据"""
        with open(path, encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    def save(self, data, path):
        """保存为json类型数据"""
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus_of_world(self):
        """获取最近一天的世界疫情"""
        home_page = self.get_content_from_url(self.home_url)
        last_data = self.parse_home_page(home_page, "getListByCountryTypeService2true")
        self.save(last_data, './爬取的数据/last_day_corona_virus.json')

    def crawl_last_day_corona_virus_of_world_of_china(self):
        """获取最近一天的世界疫情"""
        home_page = self.get_content_from_url(self.home_url)
        last_data_of_china = self.parse_home_page(home_page, 'getAreaStat')
        self.save(last_data_of_china, './爬取的数据/last_day_corona_virus_of_china.json')

    def crawl_corona_virus_of_world(self):
        """获取2020.1.23以来世界各国疫情信息"""
        total_data = self.load('./爬取的数据/last_day_corona_virus.json')
        corona_virus = self.parse_statistics_data(total_data, '正在采集世界各国的疫情信息：')
        self.save(corona_virus, './爬取的数据/corona_virus.json')

    def crawl_corona_virus_of_china(self):
        """获取中国疫情信息"""
        china_data = self.load('./爬取的数据/last_day_corona_virus_of_china.json')
        corona_virus_of_china = self.parse_statistics_data(china_data, '正在采集中国各省的疫情信息：')
        self.save(corona_virus_of_china, './爬取的数据/corona_virus_of_china.json')


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.crawl_last_day_corona_virus_of_world()
    spider.crawl_last_day_corona_virus_of_world_of_china()
    spider.crawl_corona_virus_of_world()
    spider.crawl_corona_virus_of_china()
