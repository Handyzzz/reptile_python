#!/Users/handyzzz/.venv/p352/bin python
import requests
import random
from bs4 import BeautifulSoup
import ip_tools
import ip_pool
import time
import add_line_to_file
from add_line_to_file import add_line

def splider_data():

    ip_list = ip_tools.get_ip_list_from_web()
    agent_list = ip_tools.get_agent_list()
    data_dic = {}
    for i in range(10001, 20001, 1):
        # 定时器

        url = 'https://www.douban.com/group/%d/' % i
        web_data = ip_pool.use_random_ip_request(url, 3, ip_list, agent_list)

        # print(web_data.status_code)
        soup = BeautifulSoup(web_data, 'lxml')

        data_list = []
        titles = soup.select('head > title')
        title = ''
        for temp in titles:
            if temp.string:
                title = temp.string
        num = ''
        divlist = soup.find_all(class_='mod side-nav')
        for div in divlist:
            a_list = div.find_all('a')
            if a_list[0].string:
                num = a_list[0].string

        data_list.append(title)
        data_list.append(num)
        data_list.append(url)

        data_dic['%d' % i] = data_list

        # 按行添加暂时无法使用
        # add_line_to_file.add_line(data_list)

        # 观察
        if len(title) > 0:
            warn = 'success'
        else:
            warn = 'invalid'

        print(i, warn)

    return data_dic

