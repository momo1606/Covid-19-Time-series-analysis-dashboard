from flask import Flask,render_template
import csvdata
import json
app = Flask(__name__)


@app.route('/')
def home():
    sarima_cin, pyhat_cin, pyl_cin, pyu_cin= csvdata.fetchpred('cin')
    print(pyhat_cin)
    sarima_cmh, pyhat_cmh, pyl_cmh, pyu_cmh = csvdata.fetchpred('cmh')
    sarima_din, pyhat_din, pyl_din, pyu_din = csvdata.fetchpred('din')
    sarima_dmh, pyhat_dmh, pyl_dmh, pyu_dmh = csvdata.fetchpred('dmh')
    sarima_gmale, pyhat_gmale, pyl_gmale, pyu_gmale = csvdata.fetchpred('gmale')
    sarima_gfemale, pyhat_gfemale, pyl_gfemale, pyu_gfemale = csvdata.fetchpred('gfemale')
    sarima_com_ab, pyhat_com_ab, pyl_com_ab, pyu_com_ab = csvdata.fetchpredcom('com_ab')
    sarima_com_pr, pyhat_com_pr, pyl_com_pr, pyu_com_pr = csvdata.fetchpredcom('com_pr')
    return render_template('index.html',sarima_cin=json.dumps(sarima_cin),pyhat_cin=json.dumps(pyhat_cin),
                           pyl_cin=json.dumps(pyl_cin), pyu_cin=json.dumps(pyu_cin),sarima_cmh=json.dumps(sarima_cmh),
                           pyhat_cmh=json.dumps(pyhat_cmh),pyl_cmh=json.dumps(pyl_cmh), pyu_cmh=json.dumps(pyu_cmh),
                           sarima_din=json.dumps(sarima_din),pyhat_din=json.dumps(pyhat_din),
                           pyl_din=json.dumps(pyl_din), pyu_din=json.dumps(pyu_din),
                           sarima_dmh=json.dumps(sarima_dmh),pyhat_dmh=json.dumps(pyhat_dmh),
                           pyl_dmh=json.dumps(pyl_dmh), pyu_dmh=json.dumps(pyu_dmh),sarima_gmale=json.dumps(sarima_gmale),
                           pyhat_gmale=json.dumps(pyhat_gmale),pyl_gmale=json.dumps(pyl_gmale),
                           pyu_gmale=json.dumps(pyu_gmale),sarima_gfemale=json.dumps(sarima_gfemale),
                           pyhat_gfemale=json.dumps(pyhat_gfemale),pyl_gfemale=json.dumps(pyl_gfemale),
                           pyu_gfemale=json.dumps(pyu_gfemale),sarima_com_ab=json.dumps(sarima_com_ab),
                           pyhat_com_ab=json.dumps(pyhat_com_ab),pyl_com_ab=json.dumps(pyl_com_ab),
                           pyu_com_ab=json.dumps(pyu_com_ab),sarima_com_pr=json.dumps(sarima_com_pr),
                           pyhat_com_pr=json.dumps(pyhat_com_pr),pyl_com_pr=json.dumps(pyl_com_pr),
                           pyu_com_pr=json.dumps(pyu_com_pr))


if __name__ == '__main__':
    app.run(port=1123)
