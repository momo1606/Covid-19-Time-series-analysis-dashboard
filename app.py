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
    sarima_com_ab, pyhat_com_ab, pyl_com_ab, pyu_com_ab = csvdata.fetchpredcom('com_ab')
    sarima_com_pr, pyhat_com_pr, pyl_com_pr, pyu_com_pr = csvdata.fetchpredcom('com_pr')
    actual_cin=[189325, 197496, 206405, 215709, 225560, 235447, 245418, 255401,265388, 275373, 285369, 296325, 307783, 319712, 331214]
    actual_cmh=[ 66012,  68373,  70660,  73220,  76153,  78579,  81318,  84325,86878,  89137,  92391,  95998,  99491, 102918, 106308]
    actual_din=[5370, 5574, 5791, 6051, 6324, 6618, 6905, 7111, 7442, 7721, 8078,8474, 8860, 9171, 9496]
    actual_dmh=[2276, 2352, 2455, 2577, 2700, 2839, 2959, 3050, 3159, 3279, 3428,3580, 3707, 3820, 3940]
    actual_gmale=[40682, 42211, 43679, 45084, 46652, 48444, 49943, 51590, 53443,54979, 56378, 58397, 60600, 62682, 64756]
    actual_gfemale=[24448, 25430, 26294, 27176, 28168, 29309, 30246, 31338, 32492,33509, 35387, 36621, 38025, 39436, 40789]
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
                           pyu_com_pr=json.dumps(pyu_com_pr),actual_cin=json.dumps(actual_cin),
                           actual_cmh=json.dumps(actual_cmh),actual_din=json.dumps(actual_din),actual_dmh=json.dumps(actual_dmh),
                           actual_gmale=json.dumps(actual_gmale),actual_gfemale=json.dumps(actual_gfemale))


if __name__ == '__main__':
    app.run(port=1123)
