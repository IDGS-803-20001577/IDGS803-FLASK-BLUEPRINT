from flask import Blueprint

maestros = Blueprint('maestros',__name__)


@maestros.route('/getMaestro',methods=['GET'])
def getMaestro():
    return {'key':'Maestros'}