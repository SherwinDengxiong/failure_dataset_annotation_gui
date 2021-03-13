import pandas as pd
import numpy as np
import os
def readdict(dictionfile):
    df=pd.read_csv(dictionfile,header=None,sep=',')
    dictionary=np.array(df.T)

    dict=[]

    for i,titlename in enumerate(dictionary):
        tempdict=[]
        for j,background in enumerate(dictionary[i]):
            # print(background)
            if background is np.nan:
                continue
            else:
                tempdict.append(background)
        tempdict.sort()
        dict.append(tempdict)
    dict=np.array(dict)
    return dict[0][1:],dict[1][1:],dict[2][1:],dict[3][1:],dict[4][1:],dict[5][1:]


os.rename('C:/Users/dengx/PycharmProjects/Annotation-GUI-App-master/beauty1.mp4','C:/Users/dengx/PycharmProjects/Annotation-GUI-App-master/beauty_1.mp4')



