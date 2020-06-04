from flask import Flask,render_template
import csvdata
import json
app = Flask(__name__)


@app.route('/')
def home():
    sarima_cin, pyhat_cin, pyl_cin, pyu_cin= csvdata.fetchpred()
    print(len(sarima_cin))
    return render_template('index.html',sarima_cin=json.dumps(sarima_cin),pyhat_cin=json.dumps(pyhat_cin), pyl_cin=pyl_cin, pyu_cin=pyu_cin)


if __name__ == '__main__':
    app.run()
