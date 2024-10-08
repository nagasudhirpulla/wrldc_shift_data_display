from flask import Flask, render_template, request
from wtforms import Form, validators, DateTimeField
from src.app.shiftDataFetcher import getShiftData
from src.config.appConfig import loadAppConfig

app = Flask(__name__)
# initialize config from JSON
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

if __name__ == '__main__':
    app.run(host=appConf.host, port=appConf.port, debug=True)