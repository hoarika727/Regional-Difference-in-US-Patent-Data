from zipfile import ZipFile
import os
from datetime import datetime 
import pandas as pd
import numpy as np

filepath_patent = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/zipped_data/patent.tsv.zip'
filepath_brf = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/zipped_data/brf_sum_text_2020.tsv.zip'
filepath_claim = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/zipped_data/claim_2020.tsv.zip'
filepath_desc = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/zipped_data/detail-desc-text-2020.tsv.zip'

def unzip(filepath, dir):
    with ZipFile(filepath,'r') as zip_ref:
        zip_ref.extractall(dir)

#unzip(filepath_patent,'data')

mdir = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/'
rawfolder = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/raw/'
folder = '/Users/kayinho/git/Regional-Difference-in-US-Patent-Data/data/'

N = 500
lines  = []
with open(os.path.join(folder,'patent.tsv'),'r') as file:
    for i in range(N):
        line = file.readline()
        line = line.replace('"','')
        line = line.rstrip('\n')
        lines.append(line)

df = np.vstack(lines)
print(df[0])

start = datetime.now()
with open(os.path.join(folder,'patent.tsv'),'r') as file1:
    lines = file1.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].replace('\t', ',').rstrip('\n')
    print(lines[0:5])
end = datetime.now()
print('time needed: ', end - start)

start3 = datetime.now()
df3 = pd.DataFrame([line.split(',') for line in lines[1:]], columns=[lines[0].split(',')])
print(df3[0:5])
end3 = datetime.now()
print('time needed: ', end3 - start3)

df1 = pd.read_csv(os.path.join(folder,'patent.tsv'),sep='\t',header=0, nrows=500)

start2 = datetime.now()
df_patnt = pd.read_csv(os.path.join(folder,'patent.tsv'),sep='\t',header=0)
end2 = datetime.now()
pc_patent = int(len(df_patnt)*0.01)
df_patent_1pc = df_patnt[0:pc_patent]
print('time needed: ', end2 - start2)
print(df_patent_1pc)

os.chdir(folder)
df_patent_1pc.to_csv('patent_1pc.csv', index=False)

#unzip(filepath_brf,'raw')
start3 = datetime.now()
df_brf = pd.read_csv(os.path.join(rawfolder,'brf_sum_text_2020.tsv'),sep='\t',header=0)
pc_brf = int(len(df_brf)*0.01)
df_brf_1pc = df_brf[0:pc_brf]
end3 = datetime.now()
print('time needed: ', end3 - start3)
print(df_brf_1pc)

df_brf_1pc.to_csv('brf_sum_text_2020_1pc.csv', index=False)

#unzip(filepath_claim,'raw')
df_claim = pd.read_csv(os.path.join(rawfolder,'claims_2020.tsv'),sep='\t',header=0)
pc_claim = int(len(df_claim)*0.01)
df_claim_1pc = df_claim[0:pc_claim]

df_claim_1pc.to_csv('claims_2020_1pc.csv', index=False)

#unzip(filepath_desc,'raw')
df_desc = pd.read_csv(os.path.join(rawfolder,'detail-desc-text-2020.tsv'),sep='\t',header=0)
pc_desc = int(len(df_desc)*0.01)
df_desc_1pc = df_desc[0:pc_desc]

df_desc_1pc.to_csv('detail-desc-text-2020_1pc.csv', index=False)

#os.remove(rawfolder)
