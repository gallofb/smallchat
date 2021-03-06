from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:491001@127.0.0.1/Courier', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        # self.config.from_pyfile('config/base_setting.py')
        # if "ops_config" in os.environ:
        self.config.from_pyfile('config/%s_setting.py' % "local")
        # import common.models.user.data
        Base.metadata.create_all(bind=engine)
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd() + "/web/templates/", root_path=os.getcwd())
manager = Manager(app)

# export ops_config=local||production && python manager.py runserver