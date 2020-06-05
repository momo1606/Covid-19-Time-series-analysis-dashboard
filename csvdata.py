import pandas as pd


def fetchpred(typ):
    dfcovid = pd.read_csv("covid.csv")
    df = pd.read_csv(str(typ)+"_pred.csv")
    temp = dfcovid[str(typ)].tolist()
    sarima=[]+temp
    pyhat=[]
    pyl=[]
    pyu =[]
    sarima=sarima+df.sarima.tolist()
    pyhat=pyhat+df.pyhat.to_list()
    pyl=pyl+df.pyl.to_list()
    pyu=pyu+df.pyu.to_list()
    return [sarima,pyhat,pyl,pyu]
