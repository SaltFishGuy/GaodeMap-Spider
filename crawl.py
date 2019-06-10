import requests
from lxml import etree
import csv

def get_html():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    # house_area=input("请输入房源位置")

    url = 'http://gz.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000'
    page = 0
    csv_file = open('renting.csv','w',encoding='utf-8-sig')#文件创建
    writer = csv.writer(csv_file,dialect='excel')#写入文件对象
    while True:
        page+=1
        response = requests.get(url.format(page=page),headers=headers)
        response=response.text
        html = etree.HTML(response)
        house_list = html.xpath("//ul[@class='list']/li/a") #房源信息
        print("正在下载网页",url.format(page=page))
        #page_a_list = html.xpath('//a[@class="next"]/span/text()')
        #if page_a_list != None:
            #str_page = str(page_a_list)
            #if '下一页' in str_page:
        write_file(house_list,writer)
        #     else :
        #         write_file(house_list,writer)
        #         csv_file.close()
        #         break
        # else :
        #     write_file(house_list,writer)
        if not house_list:
            csv_file.close()
            break

def write_file(house_list,writer):
    for house in house_list:
        if house!=None:
            house_title = house.xpath('normalize-space(./div[@class="img"]/img[1]/@alt)')
            house_info_list=house_title.split()
            house_location = house_info_list[1]
            house_url = house.xpath('normalize-space(./@href)')
            writer.writerow([house_title,house_location,house_url])

if __name__ == '__main__':
    get_html()
