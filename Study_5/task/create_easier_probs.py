import pandas as pd

df=pd.DataFrame()

s1=['snorkel.png']*60+['train.png']*60+['north.png']*60+['tophat']*60+['compass.png']*205+['apple.png']*45+['hammer.png']*45

df['s1_image']=s1

df.to_csv('just_s1.csv')