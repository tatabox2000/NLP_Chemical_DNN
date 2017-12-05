import numpy as np
import pandas as pd
import
def calc_bit(df):
    print(df['cactvs_fingerprint'])
    num =list('0101001001010101011111')
    print(num)
    array = np.array(num)
    print(array)


if __name__ == '__main__':
    df = pd.read_csv('connect_result.csv',dtype={'cactvs_fingerprint':'object'})
    calc_bit(df)