# -*- coding: utf-8 -*-
# @Time : 2020/3/18 21:59
# @Author : 超人不会飞
# @FileName: htmltopdf.py
# @Email : 752505176@qq.com
# @Github：https://github.com/zhongchaocheng
# @Blog ：http://752505176.xyz

import pdfkit


'''将网页url生成pdf文件'''
def url_to_pdf(url, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'E:\wkhtmltox\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_url(url, to_file, configuration=config)
    print('完成')


'''将html文件生成pdf文件'''
def html_to_pdf(html, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'E:\wkhtmltox\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_file(html, to_file, configuration=config)
    print('完成')



'''将字符串生成pdf文件'''
def str_to_pdf(string, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'E:\\wkhtmltox\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_string(string, to_file, configuration=config)
    print('完成')

if __name__ == '__main__':
    # 这里使用百度作示范
    url_to_pdf(r'https://www.baidu.com/', 'out_1.pdf')
    #html_to_pdf('sample.html', 'out_2.pdf')
    #str_to_pdf('This is test!', 'out_3.pdf')
