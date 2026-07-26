# -*- coding = utf-8 -*-

import logging
#日志的使用

#创建一个日志器
logger = logging.getLogger('logger')
#设置日志等级
logger.setLevel(logging.DEBUG)
#创建所需的处理器
handler = logging.FileHandler('all.log')
#设置处理器的日志等级
handler.setLevel(logging.DEBUG)
# #创建格式器，并指定日志格式
formater = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formater)
#根据程序创建过滤器
filer = logging.Filter(name='logger')
#向处理器添加上一步创建的格式器
handler.addFilter(filer)
#将上述的处理器添加到日志器
logger.addHandler(handler)
#打印输出日志
logger.debug('debug message')