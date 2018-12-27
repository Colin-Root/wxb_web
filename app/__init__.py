from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from config import config
#from .main import main as main_blueprint

db = SQLAlchemy()

# create_app是程序的工厂函数，参数就是配置类的名字
# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config])
#     config[config].init_app(app)
#     db.init_app(app)
#     #在工厂函数中注册蓝本main
#     app.register_blueprint(main_blueprint)
#     return app

