from web.controllers.index import route_index
from web.controllers.user.User import route_user
# from web.controllers.blueprint import pr
from application import app

app.register_blueprint(route_index,url_prefix = "/")
app.register_blueprint(route_user,url_prefix = '/user')
# app.register_blueprint(pr,url_prefix = '/prac')