#!/Users/handyzzz/.venv/p352/bin python
import re
import requests
import random
import ip_tools
from ip_tools import get_agent_list
from ip_tools import get_ip_list_from_web

def use_random_ip_request(url, timeout, ip_list, agent_list):

    # 超时次数
    timeout_num = 0
    # 更换IP次数
    change_ip_num = 0

    while timeout_num < 10:
        try:

            ran_user = random.choice(agent_list)
            headers = {'User-Agent': ran_user}

            proxies = ip_tools.get_random_ip(ip_list)

            print(proxies)
            result = requests.get(url, headers=headers, timeout=timeout, proxies=proxies)
            print(result.status_code)
            if result.status_code == 200:
                print('请求成功 状态码%d' % result.status_code)
                return result.text
            else:
                print('使用ip %(python)s 请求错误' % proxies)
                print('begin next URL...')
                return ''
        except:
            timeout_num += 1
            print('网络请求超时 开始递归 第%d次' % timeout_num)
    else:
        if timeout_num >= 10:
            print('网络超时达到上限10次')
        print('begin next URL...')
        return ''

# 调试代码 测试是否是ip池失效
# ip_list = ip_tool.get_ip_list_from_web()
# agent_list = ip_tool.get_agent_list()
# url = 'https://www.baidu.com'
# url = 'https://www.douban.com/group/10001/'
# result_text = use_random_ip_request(url, 2, ip_list, agent_list)
# print(result_text)

