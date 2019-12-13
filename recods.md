1.设置pipenv 安装在项目根目录  set WORKON_HOME=PIPENV_VENV_IN_PROJECT, 或set PIPENV_VENV_IN_PROJECT=true  pipenv shell  显示的激活虚拟环境
2.用pipenv install xxx， Pipfile 自动记录安装包  
3.pipenv install python-dotenv,  添加环境变量管理  手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量
4.flaskenv用来存储和Flask相关的公开环境变量,而.env用来存储包含敏感信息的环境变量
5.pycharm 搜索 file types, 隐藏.env文件