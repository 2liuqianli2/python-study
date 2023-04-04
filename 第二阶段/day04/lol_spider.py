from time import sleep

import requests
import pymysql




def get_html(url):
    header={
        "Accept": "text/css,*/*;q=0.1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    res=requests.get(url,header)
    # print(res)
    return res

def get_html_js(url):
    res=get_html(url)

    return res.json()


def save_hero_to_sql(data):
    conn=get_db_con()

    #插入英雄
    data1 = data.get('hero')
    # print(data1)
    sql="insert into heros(heros_id,name,shortBio) values ('%s','%s','%s');"%(data1.get("heroId"),data1.get("name"),data1.get("shortBio"))
    excute_sql_insert(conn,sql)


    #插入皮肤
    datas = data.get('skins')
    for data2 in datas:
        sql = "insert into skin(skinld,herold,name,mainlmg) values ('%s','%s','%s','%s');" % (
        data2.get("skinId"), data2.get("heroId"), data2.get("name"), data2.get("mainImg"))
        print(data2.get("heroId"),data2.get("skinId"),data2.get("mainImg"))
        excute_sql_insert(conn, sql)

    #插入技能
    datas = data.get('spells')
    for data3 in datas:
        sql = "insert into spell(heroId,name,description,abPath) values ('%s','%s','%s','%s');" % (
        data3.get("heroId"), data3.get("name"), data3.get("description"), data3.get("abilityIconPath"))
        excute_sql_insert(conn, sql)


    colse_db_con(conn)


def get_db_con():
    conn=pymysql.Connect(host="localhost",port=3306,
                         user="root",password="mysql123",charset="utf8",
                         database="lol")
    return conn

def colse_db_con(conn):
    conn.close()

def execute_sql(conn,sql):
    cursor=conn.cursor()
    cursor.execute(sql)
    return cursor

def excute_sql_insert(conn,sql):
    cursor=execute_sql(conn,sql)
    conn.commit()


def execute_sql_query(conn,sql):
    cursor = execute_sql(conn, sql)
    return cursor.fetchall()





if __name__ == '__main__':
    url="https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2800834"
    url1="https://game.gtimg.cn/images/lol/act/img/js/hero/%s.js?ts=2800838"
    hero_numbers=get_html_js(url).get('hero')
    # print(hero_numbers)

    # hero_id=[]
    # hero_list = {
    #
    # }
    for i in hero_numbers:
        i=i.get('heroId')
        print(i)
        sleep(1)
        data=get_html_js(url1%i)
        # print(data)
        save_hero_to_sql(data)

    #
    # for i in hero_id:
    #
    #     hero_name=get_html_js(url1%i).get('hero').get('name')
    #     hero_shortBio=get_html_js(url1%i).get('hero').get('shortBio')
    #     hero_spell=get_html_js(url1%i).get('spells')
    #     for i in hero_spell:
    #         name=i.get('熔岩护盾')
    #         description=i.get('description')
    #         img=i.get('abilityIconPath')



