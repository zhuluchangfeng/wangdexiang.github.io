import pandas as pd
import numpy as np
"""
各种距离函数 欧氏，切比雪夫，汉明，曼哈顿，马氏，标欧氏
相似度函数 余弦距离，编辑距离
"""

def cxdisc(x,y):
    """切比雪夫"""
    return (x - y).abs().max()
df1 = np.array([[1, 0], [0, 1], [1, 1], [2, 6]])
df2 = np.array([[1, 1], [-1, -1], [1, 3**0.5]])
def cosdisc(df1, df2) :
    """
    余弦距离
    :param df1: np.array
    :param df2: np.array
    :return: matrix
    """
    dm1 = np.matrix(df1)
    dm2 = np.matrix(df2)
    disc1 = np.sqrt((df1*df1).sum(axis=1))
    disc2 = np.sqrt((df2*df2).sum(axis=1))
    disc1 = np.matrix(disc1)
    disc2 = np.matrix(disc2)
    return (dm1*dm2.T)/(disc1.T*disc2)
# def cosdisc1(df1,df2):
#     """先变单位向量的"""
#     df1=df1/np.array([np.sqrt((df1**2).sum(axis=1))]).T
#     df2=df2/np.array([np.sqrt((df2**2).sum(axis=1))]).T
#     dm1=np.matrix(df1)
#     dm2=np.matrix(df2)
#     return (dm1*dm2.T)
df = pd.DataFrame({'f1':[1,2,3,4,5],'f2':[1,2,1,2,1],'f3':[5,1,3,4,2],'f4':[11,1,2,5,8]})
def mkdisc(x,y,n):
    """闵可夫斯基距离"""
    return np.sum((x-y)**n)**(1/n)

def mdisc(x,y,df):
    """马氏距离"""
    s=df.cov().values
    s_=np.linalg.inv(s)
    return np.dot(np.dot(x.values,s_),y.values.T)
def edisc(x,y):
    disc = sum((x-y)**2)
    return disc**0.5
def stdedisc(x,y,df):
    """标欧氏 全体标准化"""
    m=df.mean(axis=0)
    s=df.std(axis=0)
    x=x-m/s
    y=y-m/s
    return edisc(x,y)

s1='sfesxdc'
s2='zfesaf '
def hdisc(s1,s2):
    """汉明顿距离"""
    n=0
    for i in range(len(s1)):
        if ord(s1[i])==ord(s2[i]):
            n+=1
    return n
s1 = 'kat'
s2 = 'kitte'
def editdisc(s1, s2):
    """编辑距离
    :param str:
    :param str:
    :return: int:
    """
    df=np.eye(len(s2)+1,len(s1)+1)
    df[:,0]=range(len(s2)+1)
    df[0,:]=range(len(s1)+1)
    for i in range(len(s1)):
        for j in (range(len(s2))):
            if ord(s1[i])==ord(s2[j]):
                cost=0
            else:
                cost=1
            df[j+1,i+1]=min(df[j+1,i]+1,df[j,i+1]+1,df[j,i]+cost)
    return df[-1,-1]
print(editdisc('kite','kittle'))
