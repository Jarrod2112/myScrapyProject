import pandas as pd

#read in csv results
jegs = pd.read_csv('spreadsheets/jegs.csv')
karl = pd.read_csv('spreadsheets/karl.csv')
pace = pd.read_csv('spreadsheets/pace.csv')
speedway = pd.read_csv('spreadsheets/speedway.csv')

#create list of frames
frames = [jegs, karl, pace, speedway]

#concatenate frames
results = pd.concat(frames)

#write to csv
results.to_csv('results.csv')
