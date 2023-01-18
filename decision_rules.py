import numpy as np
import pandas as pd

##############################
# Criterion of Pessimisim    #
# Maximin (Best of the Worst)#
##############################
def MaxiMin(DecisionTable, alt_label, evt_label):
    rule="MaxiMin"
    matrix = pd.DataFrame(DecisionTable)
    df = pd.DataFrame(matrix)
    list_maximin = []
    event_label = 0
    alternative_label = 0   

    list_maximin = df.min(axis=1).tolist()
    alternative_label = list_maximin.index(max(list_maximin))
    event_label = df.loc[alternative_label].values.tolist().index(min(df.loc[alternative_label].values.tolist()))
    
    return rule, alt_label[alternative_label], evt_label[event_label], max(list_maximin)


##############################
# Criterion of Optimism      #
# Maximax (Best of the Best) #
##############################
def MaxiMax(DecisionTable, alt_label, evt_label):
    rule="MaxiMax"
    matrix = pd.DataFrame(DecisionTable)
    df = pd.DataFrame(matrix)
    list_maximax = []
    event_label = 0
    alternative_label = 0
    
    list_maximax = df.max(axis=1).tolist()
    alternative_label = list_maximax.index(max(list_maximax))
    event_label = df.loc[alternative_label].values.tolist().index(max(df.loc[alternative_label].values.tolist()))
    
    return rule, alt_label[alternative_label], evt_label[event_label], max(list_maximax)
               
############################
# Criterion of Rationality #
# Laplace                  #
############################
def Laplace(DecisionTable, alt_label, evt_label):
    rule="Laplace"
    df = pd.DataFrame(DecisionTable)
    row, col = df.shape

    df["mean"] = df.mean(axis=1)
    list_laplaceValues = df["mean"].tolist()
    alternative_label = list_laplaceValues.index(max(list_laplaceValues))

    return rule, alt_label[alternative_label], max(list_laplaceValues)


##############################
# Criterion of Optimism      #
# Minimax (Worst Regret)     #
##############################
def MiniMax(DecisionTable, alt_label, evt_label):
    rule="MiniMax"
    df = pd.DataFrame(DecisionTable)
    row, col = df.shape
    regretTable = pd.DataFrame()

    #Initialize Regret Table
    for i in range(col):
        maxValue = df[i].max()
        regretTable[i] = df[i].apply(lambda x: (maxValue - x) if 1==1 else x)

    list_maxValues = regretTable.max(axis=1).tolist()
    alternative_label = list_maxValues.index(min(list_maxValues))
    event_label = regretTable.loc[alternative_label].values.tolist().index(max(regretTable.loc[alternative_label].values.tolist()))
    
    return rule, alt_label[alternative_label], min(list_maxValues), regretTable



############################
#     Expected Pay off     #
############################
def Exp_Value(DecisionTable, alt_label, evt_label,likelihood):
    rule="Exp_Value"
    df = pd.DataFrame(DecisionTable)
    row, col = df.shape
    
    for i in range(col):
        df[i] = df[i].apply(lambda x: (likelihood[i][0]*x) if 1==1 else x)

    df["Expected Payoff"] = df.sum(axis=1)
    list_maxValues = df.max(axis=1).tolist()
    alternative_label = list_maxValues.index(max(list_maxValues))
        
    return rule, alt_label[alternative_label], max(list_maxValues)
