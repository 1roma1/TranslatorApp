from flask import Blueprint, render_template, request

from .request import make_request
from .text_processing import preprocess_input, preprocess_output

bp = Blueprint('translate', __name__, url_prefix='/')


@bp.route('/', methods=('GET', 'POST'))
def register():
    content = {'input_text': '', 'output_text': '', 'curr_lang': 'eng'}

    if request.method == 'POST':
        content['input_text'] = request.form['inputText']
        content['curr_lang'] = request.form['currLang']

        input_text = preprocess_input(content['input_text'])

        if request.form['currLang'] == "eng":
            for sentence in input_text:
                content['output_text']+=make_request("engru_transformer", sentence)+" "
        else:
            for sentence in input_text:
                content['output_text']+=make_request("rueng_transformer", sentence)+" "

        
        content['output_text'] = preprocess_output(content['output_text'])

    return render_template('translation/translation.html', content=content)