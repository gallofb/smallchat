from flask import Blueprint,render_template,request,jsonify,make_response,redirect,g
import json
from application import db
# from common.libs.helpler import ops_render
# from common.libs.UrlManager import UrlManager
# from common.models.user import User
from common.models.user.User import TesUsr,User
# from common.libs.user.UserService import UserService
# from application import app
# from wtforms.validators import Emailid
route_user = Blueprint('user_page',__name__ )


@route_user.route("/user", methods=['GET','POST'])
def login():
    info = User.query.filter_by(uid=1).first()

    if request.method == 'GET':
        dicta =  {"a":1,"b":2}
        # print(6)
        # print(jsonify(dict))
        # print(info.email)
        print(type(info))
        print("5555")
    if request.method == 'POST':
        # c = request.values
        # print(c)
        #
        formdatas = request.form
        print(666)
        print(formdatas['sex'])
        formation = User.query.filter_by(uid=1).first()
        formation.email =formdatas['email']
        db.session.commit()
    return render_template('information.html',info=info)

        # db.session.commit()
        # print(formdatas)
        # print(formdatas['sex'])
        # print(formdatas['school'])
        # print(formdatas['phone'])
        # print(formdatas['email'])
        # print(formdatas['address'])
    # return render_template('information.html')
"""
@route_user.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "GET":
        return ops_render("user/edit.html", {"current": "edit"})

    resp = {'code': 200, 'msg': "操作成功！", 'data': {}}

    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''

    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的姓名！'
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入符合规范的邮箱！'
        return jsonify(resp)

    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add(user_info)
    db.session.commit()

    return jsonify(resp)

"""

# $.ajax({
#     url: common_ops.buildUrl("/user/edit"),
#     type: 'POST',
#     data: data,
#     dataType: 'json',
#     success: function(res){
#     btn_target.removeClass("disabled");
# var
# callback = null;
# if (res.code == 200)
# {
#     callback = function()
# {
#     window.location.href = window.location.href;
# }
# }
# common_ops.alert(res.msg, callback);
# }
# });
