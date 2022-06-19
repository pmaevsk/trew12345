from flask import Blueprint
from flask import request, render_template
import requests
import json

form_blueprint = Blueprint('form_blueprint', __name__)


from app import db  # prevent cyclic import
from app import MyForm


@form_blueprint.route('/')
def index():
    return ('<a class="button" href="/forms">Submit form</a>''<br>'
            '<a class="button" href="/forms/confirmed">List my submitted forms</a>''<br>')



@form_blueprint.route('/forms/', methods=['POST', 'GET'])
def forms():
    if request.method == 'POST':
        data_json = {"form": []}
        data_json['form'].append(request.form.to_dict())
        amount = len(request.form.to_dict())
        for i in range(amount):
            key = 'input-{}'.format(i)
            if data_json["form"][0][key] == '':
                del data_json["form"][0][key]
            else:
                pass
        if data_json["form"][0] != {}:
            data = MyForm(data_json)
            db.session.add(data)
            db.session.commit()
    return render_template("forms/forms.html")

@form_blueprint.route('/forms/confirmed', methods=['GET'])
def confirmed_forms():
    forms = MyForm.query.all()
    return render_template('forms/subforms.html', content={'my_forms': forms})