from flask import Flask,render_template
import csvdata
import json
app = Flask(__name__)


@app.route('/')
def home():
    sarima_cin, pyhat_cin, pyl_cin, pyu_cin= csvdata.fetchpred('cin')
    sarima_cmh, pyhat_cmh, pyl_cmh, pyu_cmh = csvdata.fetchpred('cmh')
    sarima_din, pyhat_din, pyl_din, pyu_din = csvdata.fetchpred('din')
    sarima_dmh, pyhat_dmh, pyl_dmh, pyu_dmh = csvdata.fetchpred('dmh')
    sarima_gmale, pyhat_gmale, pyl_gmale, pyu_gmale = csvdata.fetchpred('gmale')
    sarima_gfemale, pyhat_gfemale, pyl_gfemale, pyu_gfemale = csvdata.fetchpred('gfemale')
    # sarima_com_ab, pyhat_com_ab, pyl_com_ab, pyu_com_ab = csvdata.fetchpredcom('com_ab')
    # sarima_com_pr, pyhat_com_pr, pyl_com_pr, pyu_com_pr = csvdata.fetchpredcom('com_pr')
    actual_cin=[439005,454973,471895,489191,507743,527649,547108]
    actual_cmh=[134146,137260,141150,145991,151015,156333,161826]
    actual_din=[12341,12806,13224,13631,14015,14425,14805]
    actual_dmh=[4943,5018,5090,5199,5290,5376,5436]
    actual_gmale=[81682,83996,85966,88304,91289,94410,97647]
    actual_gfemale=[51350,52774,54031,55592,57476,59397,61494]
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
                           pyu_gfemale=json.dumps(pyu_gfemale),
                           # ,sarima_com_ab=json.dumps(sarima_com_ab),
                           # pyhat_com_ab=json.dumps(pyhat_com_ab),pyl_com_ab=json.dumps(pyl_com_ab),
                           # pyu_com_ab=json.dumps(pyu_com_ab),sarima_com_pr=json.dumps(sarima_com_pr),
                           # pyhat_com_pr=json.dumps(pyhat_com_pr),pyl_com_pr=json.dumps(pyl_com_pr),
                           # pyu_com_pr=json.dumps(pyu_com_pr)
                            actual_cin=json.dumps(actual_cin),
                           actual_cmh=json.dumps(actual_cmh),actual_din=json.dumps(actual_din),actual_dmh=json.dumps(actual_dmh),
                           actual_gmale=json.dumps(actual_gmale),actual_gfemale=json.dumps(actual_gfemale)
                           )


if __name__ == '__main__':
    app.run(port=1123)
