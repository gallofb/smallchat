flask-sqlacodegen 'mysql://root:491001@127.0.0.1/Courier' --tables user --outfile "common/models/user/User.py"
flask-sqlacodegen 'mysql://root:491001@127.0.0.1/Courier' --outfile "common/models/user/User.py"

export ops_config=local&& python manage.py runserver
运行