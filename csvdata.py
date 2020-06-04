import pandas as pd


def fetchpred():
    dfcovid = pd.read_csv("covid.csv")
    df = pd.read_csv("cin_pred.csv")
    predict=df.to_dict()
    #dates=pd.date_range(start='4/1/2020', end='6/30/2020').to_list

    sarima=[]
    pyhat=[]
    pyl=[]
    pyu = []
    for j in dfcovid['cin']:
        sarima.append(j)
        pyhat.append(j)
        pyl.append(j)
        pyu.append(j)

    for i in predict['sarima']:
        sarima.append(i)
    for i in predict['pyhat']:
        pyhat.append(i)
    for i in predict['pyl']:
        pyl.append(i)
    for i in predict['pyu']:
        pyu.append(i)


    return [sarima,pyhat,pyl,pyu]
