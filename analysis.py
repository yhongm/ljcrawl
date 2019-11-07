#-*- coding: utf-8 -*-
import pandas as pd
from os import path

def parse_csv(csv_name):
    dir = path.dirname('.')
    df = pd.read_csv(path.join(dir, '%s.csv'%csv_name))
    r=df.groupby('area')
    v=r.house_price.agg(['max','min','mean','count'])
    print(v)




if __name__ == "__main__":
    print("-------------------贝壳-------------------------")
    parse_csv('beike')
    print("-------------------链家-------------------------")
    parse_csv('lianjia')

