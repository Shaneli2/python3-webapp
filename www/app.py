#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Shane li'

import logging;logging.basicConfig(level=logging.INFO)


import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


async def index(request):  # 创建一个request handler
    resp = web.Response(body='<h1> Hello, this is my 1st web site</h1>')
    # 如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    resp.content_type = 'text/html;charset=utf-8'
    return resp


# 通过localhost:8080/hello/输入一个字符串 访问
async def hello(request):
    text = '<h1>hello,%s</h1>' % request.match_info['name']
    resp = web.Response(body=text.encode('utf-8'))
    # 如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    resp.content_type = 'text/html;charset=utf-8'
    return resp


async def init(loop):  # 初始化服务器
    app = web.Application(loop=loop)  # 创建一个Application实例

    app.router.add_route('GET', '/', index)  # 用实例对request handler注册
    app.router.add_route('GET', '/hello/{name}', hello)

    srv = await loop.create_server(app.make_handler(), 'localhost', 8080)  # 创建服务器，绑定地址，端口和handler
    logging.info('server started at http://localhost:8080....')
    return srv


loop = asyncio.get_event_loop()  # 获取EventLoop
loop.run_until_complete(init(loop))  # 执行协程
loop.run_forever()  # 服务器不关闭

