import requests
import re,time
import pymysql

def Get_csdn():
    global headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    }
    url = "https://blog.csdn.net/yolo2016?type=blog"
    html = requests.get(url, headers=headers).text
    # print (html)
    result = re.findall('href="(https://blog.csdn.net/yolo2016/article/details/.*?)\".*?<h4.*?>(.*?)</h4>', html, re.S)
    return (result)

def Mysql_handle(result):
    # 打开数据库连接
    db = pymysql.Connect(
        host='192.168.1.50',
        port=3306,
        user='root',
        passwd="",
        db='test',
        charset="utf8"
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.executemany("INSERT INTO csdn(url,title) VALUES (%s,%s)", result)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        print(e)
        db.rollback()
    finally:
        sql2 = 'select * from csdn'
        cursor.execute(sql2)
        results = cursor.fetchall()
        print(results)
    # 关闭数据库连接
    db.close()

def Get_Articel(result):
    '''
    获取文章列表信息来get 文章的内容
    文章列表result内容  eg：   info=[
                                 ('https://blog.csdn.net/yolo2016/article/details/115770342', '几个高质量的运维博客收藏'),
                                 ('https://blog.csdn.net/yolo2016/article/details/115678745', '运维自动化所需要的技能？')]
    '''
    count=0
    while True:
        art_counts = len(result)
        print('=============Article Number is %s ============'% art_counts)
        for art_url,art_name in result:
            print("====URL:%s ===============>> NAME:%s "%(art_url,art_name))
            html = requests.get(art_url, headers=headers).text
            time.sleep(3)
            #print (html)
        count+=1
        print("#############第 %s 轮循环完毕##################"% (count))

if __name__ == '__main__':
    result = Get_csdn()
    Mysql_handle(result)
    Get_Articel(result)
