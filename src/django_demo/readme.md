### django 常用命令

* 创建项目
`django-admin startproject project_name`

* 运行项目
`python manage.py runserver`

* 修改端口号
`python manage.py runserver port` 

* 外部访问
```
1. 修改 setting.py ALLOWED_HOSTS的值为本机IP
2. python manage.py runserver 0.0.0.0: port
3. DEBUG为True(dev) False(prov)
```

* 创建应用
`python manage.py startapp app_name` 会在项目目录下多一个app_name的文件夹

* 个人任务django还是比价重，仅适合开发后台使用