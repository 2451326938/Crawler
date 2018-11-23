#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import psycopg2
from flask import Flask,render_template
import psycopg2.extras
import sys
reload(sys)
sys.setdefaultencoding('utf8')


app=Flask(__name__)

# @app.route('/ddd', methods=['GET'])
def tohtml():
    conn = psycopg2.connect(database="anjuke", user="postgres", password="#$0okmNJI9~@$^hTC", host="10.255.81.44",
                            port="5432")  # 连接数据库
    print "success"
    cur = conn.cursor()
    # cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT money,moneytime,moneystyle,homeaddress,telephone,img,url,homeload FROM ZHUHOME;")  # 查询表中所有值
    rows = cur.fetchall()  #接受返回结果
    i=[]
    for row in rows:
        dic={
            "money": row[0],
            "moneytime": row[1],
            "moneystyle": row[2],
            "homeaddress": row[3],
            "telephone": row[4],
            "img": row[5],
            "url": row[6],
            "homeload": row[7]
        }
        i.append(dic)
    return render_template("index.html", user=i)
    # return json.dumps({"status":"success", "data": rows})
app.add_url_rule('/', 'tohtml', tohtml)

app.run(host="0.0.0.0", debug=True, port=5000)

