from flask import Flask, render_template, request
from wtforms import Form, validators, DateTimeField
from src.app.shiftDataFetcher import getShiftData
from src.config.appConfig import loadAppConfig

# create a flask server
app = Flask(__name__)
appConf = loadAppConfig()

class ShiftDataForm(Form):
    startTime = DateTimeField(
        'Start Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired()])
    endTime = DateTimeField(
        'End Time', format='%Y-%m-%d %H:%M', validators=[validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ShiftDataForm(request.form)
    data = {}
    if request.method == 'POST' and form.validate():
        data = getShiftData(form.startTime.data, form.endTime.data)
    return render_template("index.html", form=form, data=data)

# __name__ will be __main__ only if this file is the entry point
if __name__ == '__main__':
    # run the server on this ip and port 50100
    app.run(host='0.0.0.0', port=8086, debug=True)