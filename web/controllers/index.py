from flask import Blueprint,render_template,session
route_index = Blueprint('index_page',__name__)

@route_index.route("/")
def index():
    print(666)
    return render_template('information.html')
    # return "eh"