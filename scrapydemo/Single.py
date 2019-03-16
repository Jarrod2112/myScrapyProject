import pandas as pd

#read in csv results
jegs = pd.read_csv('data/spider_data/jegs.csv')
karl = pd.read_csv('data/spider_data/karl.csv')
pace = pd.read_csv('data/spider_data/pace.csv')
speedway = pd.read_csv('data/spider_data/speedway.csv')

#create list of frames
frames = [jegs, karl, pace,speedway]

#concatenate frames
results = pd.concat(frames)

#write to csv
results.to_csv('results.csv')




		 
		 