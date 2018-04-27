from flask import Flask
from flask import render_template
from flask import request
from moduls import Cpu
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/showData')
def showData():
#    cpus = Cpu.select()
    return render_template('blank.html')

@app.route('/api',methods=['POST','GET'])
def api():
    result = {
        'status':'error',
        'data':''
    }
    if request.method == 'POST':
        data = request.form
        try:
            model = data['model']
            model_name = data['model_name']
            steeping = data['steeping']
            microcode = data['microcode']
            cpu_MHz = data['cpu_MHz']

            c = Cpu()
            c.model = model
            c.model_name = model_name
            c.steeping = steeping
            c.cpu_MHz = cpu_MHz
            c.microcode = microcode
            c.save()

            result['status'] = 'success'
            result['data'] = 'your data is saved'

        except Exception as e:
            #?
            result['data']=str(e)
    else:
        result['data'] = 'your rquest must be post'

    return json.dumps(result)

if __name__ == '__main__':
    app.run(port=8000,host="0.0.0.0",debug=True)
