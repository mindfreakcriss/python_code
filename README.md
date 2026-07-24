
### python 常见操作

* 依赖打包
```
pip freeze > requirement.txt
```

* 依赖安装
```
pip install -r requirement.txt
```

* 目前的模块内容

* numpy, pandas, requests,beautifulsoup4,redis,mysql,flask等内容

## web访问部署流程

* gunicorn 控制python脚本
```
gunicorn -D -w 4 -b 127.0.0.1:8000 server:app
```

* nginx 方向代理 gunicorn 服务
```
server {
    listen 8020;
    server_name localhost;
    root {$path}/python_code/normal_package;

    location /{
        index index.html index.htm;
        proxy_pass http://127.0.0.1:8000;
        #必要的代理头设置
    }
}
```

* 启动服务
```
sh server_start.sh
```

* 杀死进程：代码更新之后需要重启服务才行,可以使用容器进行处理
```
pkill -f "gunicorn.*server:app"
```

## 更新mac M4 环境安装出错
```
pip install llvmlite==0.44.0
pip install numba==0.61.2
pip install numpy==1.26.4
pip install -r requirements.txt
```