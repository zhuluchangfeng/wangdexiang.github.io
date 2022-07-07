import schedule
import time
import requests

from meutils.request_utils.crawler import Crawler

boot_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=43e28f3b-0c07-492c-aa37-a59abc3acf43"
url_d = {'第一财经': ['https://tophub.today/n/0MdKam4ow1',
                  '//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[2]/a/text()'],
         '百度热搜': ['https://top.baidu.com/board?tab=realtime',
                  '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div/div[2]/a/div[1]/text()']}


def send_note(title, boot_url):
    try:
        c = Crawler(url_d.get(title)[0])
    except Exception as e:
        print(e)
    strs = c.xpath(url_d.get(title)[1])
    n = 1
    text_long = f'# {title}\n'
    text_long = text_long + f'## {time.strftime("%Y/%m/%d %X")} '
    for i in strs:
        text_long = text_long + f'\n{n}. {i}'
        n += 1
    json = {
        "msgtype": "markdown",
        "markdown": {"content": text_long}
    }
    requests.post(boot_url, json=json).text


def task():
    for i in url_d:
        send_note(i, boot_url)


if __name__ == '__main__':
    schedule.every().day.at("08:15").do(task)
    while 1:
        schedule.run_pending()
        time.sleep(60)

