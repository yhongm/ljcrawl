#-*- coding: utf-8 -*-
import pandas as pd
from os import path

def parse_csv():
    dir = path.dirname('.')
    print("dir:"+path.abspath(''))

    df = pd.read_csv(path.join(dir, 'item.csv'))
    r=df.groupby('xiaoqu')
    v=r.house_price.agg(['max','min','mean','count'])
    print(v)




if __name__ == "__main__":

    parse_csv()

