from flask import Blueprint,render_template,request,jsonify,make_response,redirect,g
import json
from application import db
# from common.libs.helpler import ops_render
# from common.libs.UrlManager import UrlManager
# from common.models.user import User
from common.models.user.data import TesUsr,User
# from common.libs.user.UserService import UserService
# from application import app
# from wtforms.validators import Emailid
route_user = Blueprint('user_page',__name__ )


@route_user.route("/user", methods=['GET','POST'])
def login():
    user = User.query.all()
    print(user)
    # user =User.query.all()
    # print(user.uid)
    # if user:
    #     print("555")
    # else:
    #     print("888")
    # print(type(user))
    return "666"

# flask-sqlacodegen 'mysql://root:491001@127.0.0.1/Courier' --outfile "common/models/tes_usr.py"  --flask
# flask-sqlacodegen 'mysql://root:491001@127.0.0.1/Courier' --tables tes_usr --tfile "common/models/tes_usr.py"

