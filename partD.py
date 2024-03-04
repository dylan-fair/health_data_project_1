# Libraries
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime
import re
from scipy.stats import f_oneway

# Import Data
covid = pd.read_csv("Project 1\COVID-ctg-studies.csv")
bc = pd.read_csv("Project 1\Breast cancer-ctg-studies.csv")

# Function to calculate trial durations
def duration(df):
    syears = []
    smonths = []
    sdays = []
    cyears = []
    cmonths = []
    cdays = []
    for i in range(len(df)):
        sy, sm, sd = df['Start Date'][i].split('-')
        cy, cm, cd = df['Completion Date'][i].split('-')
        syears.append(int(sy))
        smonths.append(int(sm))
        sdays.append(int(sd))
        cyears.append(int(cy))
        cmonths.append(int(cm))
        cdays.append(int(cd))
    
    df['Start Year'] = syears
    df['Start Month'] = smonths
    df['Start Day'] = sdays
    df['Completion Year'] = cyears
    df['Completion Month'] = cmonths
    df['Completion Day'] = cdays
    
    durations = []
    for i in range(len(df)):
        durations.append((datetime(df['Completion Year'][i], df['Completion Month'][i], df['Completion Day'][i]).date() - datetime(df['Start Year'][i], df['Start Month'][i], df['Start Day'][i]).date()).days)
    
    df['Duration'] = durations


duration(covid)
duration(bc)

# Function to restrict 'Intervention' column to general categories rather than full descriptions
def general_ints(df):
    intervention = []
    for i in range(len(df)):
        intervention.append(re.search(r'(.*?):', df['Interventions'][i]).group(1))

    df['Interventions'] = intervention


general_ints(covid)
general_ints(bc)

sns.scatterplot(x='Interventions', y='Duration', data=covid).set(title='Scatterplot of COVID Trial Durations by Intervention Type')
plt.show()
sns.boxplot(x='Interventions', y='Duration', data=covid).set(title='Boxplot of COVID Trial Durations by Intervention Type')
plt.show()

sns.scatterplot(x='Interventions', y='Duration', data=bc).set(title='Scatterplot of Breast Cancer Trial Durations by Intervention Type')
plt.show()
sns.boxplot(x='Interventions', y='Duration', data=bc).set(title='Boxplot of Breast Cancer Trial Durations by Intervention Type')
plt.show()

# Function to calculate One-Way ANOVA for trial duration based on intervention type
def one_way_anova(df):
    bio = df[df['Interventions'] == 'BIOLOGICAL']
    drug = df[df['Interventions'] == 'DRUG']
    diag = df[df['Interventions'] == 'DIAGNOSTIC_TEST']
    diet = df[df['Interventions'] == 'DIETARY_SUPPLEMENT']
    other = df[df['Interventions'] == 'OTHER']
    dev = df[df['Interventions'] == 'DEVICE']
    com = df[df['Interventions'] == 'COMBINATION_PRODUCT']
    beh = df[df['Interventions'] == 'BEHAVIORAL']
    pro = df[df['Interventions'] == 'PROCEDURE']
    rad = df[df['Interventions'] == 'RADIATION']
    gen = df[df['Interventions'] == 'GENETIC']

    anova = f_oneway(bio['Duration'], drug['Duration'], diag['Duration'], diet['Duration'], other['Duration'],
                     dev['Duration'], com['Duration'], beh['Duration'], pro['Duration'], rad['Duration'], gen['Duration'])
    return anova


one_way_anova(covid) # F = 3.9515812490082385, p = 2.2678327723478264e-05
one_way_anova(bc) # F = 27.753682120551705, p = 2.615084382039912e-51
