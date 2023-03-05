from flask import Blueprint

directivos = Blueprint('directivos',__name__)


@directivos.route('/getDirec',methods=['GET'])
def getDirec():
    return {'key':'Directivos'}