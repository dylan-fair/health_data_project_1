import pandas as pd
import matplotlib.pyplot as plt

breast_cancer = pd.read_csv('Breast cancer-ctg-studies.csv')
covid = pd.read_csv('COVID-ctg-studies.csv')

interventions = covid['Interventions'].str.split('|')
covid_drugs = {}
for intervention in interventions:
    for string in intervention:
        if 'DRUG' in string:
            parced = string.split(': ')
            if parced[-1] in covid_drugs.keys():
                covid_drugs[parced[-1]] += 1
            else:
                covid_drugs[parced[-1]] = 1

# Get the top 15 items in descending order
top_15 = sorted(covid_drugs.items(), key=lambda x: x[1], reverse=True)[:15]

# Print the top 15 items
# for key, value in top_15:
#     print(f'{key}: {value}')

# Extract drug names and study counts
drugs, counts = zip(*top_15)

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.barh(drugs, counts, color='skyblue')
plt.xlabel('Number of Studies')
plt.title('Top 15 Drugs Studied Under COVID')
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.show()

breast_cancer_drugs = {}

interventions = breast_cancer['Interventions'].str.split('|')
for intervention in interventions:
    for string in intervention:
        if 'DRUG' in string:
            parced = string.split(': ')
            if parced[-1] in breast_cancer_drugs.keys():
                breast_cancer_drugs[parced[-1]] += 1
            else:
                breast_cancer_drugs[parced[-1]] = 1

# Get the top 15 items in descending order
top_15 = sorted(breast_cancer_drugs.items(), key=lambda x: x[1], reverse=True)[:15]

drugs, counts = zip(*top_15)

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.barh(drugs, counts, color='skyblue')
plt.xlabel('Number of Studies')
plt.title('Top 15 Drugs Studied For Breast Cancer')
plt.gca().invert_yaxis()  # Invert y-axis for better readability
plt.show()

covid['Start Date'] = pd.to_datetime(covid['Start Date'], format='%Y-%m-%d', errors='coerce')
covid['Start Date_month'] = pd.to_datetime(covid['Start Date'], format='%Y-%m', errors='coerce')

# Combine masks to filter trials for the desired date range in the 'covid' dataframe
covid_filtered = covid[(covid['Start Date'] >= '2020-01-01') | (covid['Start Date_month'] >= '2020-01-01')]

# Drop the temporary column used for 'yyyy-mm' format
covid_filtered.drop(columns=['Start Date_month'], inplace=True)

# Repeat the same process for the 'breast_cancer' dataframe

# Convert 'Start Date' to datetime format for both 'yyyy-mm-dd' and 'yyyy-mm' formats
breast_cancer['Start Date'] = pd.to_datetime(breast_cancer['Start Date'], format='%Y-%m-%d', errors='coerce')
breast_cancer['Start Date_month'] = pd.to_datetime(breast_cancer['Start Date'], format='%Y-%m', errors='coerce')

# Combine masks to filter trials for the desired date range in the 'breast_cancer' dataframe
breast_cancer_filtered = breast_cancer[(breast_cancer['Start Date'] >= '2020-01-01') | (breast_cancer['Start Date_month'] >= '2020-01-01')]

# Drop the temporary column used for 'yyyy-mm' format
breast_cancer_filtered.drop(columns=['Start Date_month'], inplace=True)

# Group by two-month periods and count the number of trials
covid_timeline = covid_filtered.groupby(pd.Grouper(key='Start Date', freq='2M')).size()
breast_cancer_timeline = breast_cancer_filtered.groupby(pd.Grouper(key='Start Date', freq='2M')).size()

# Plot the line graph
plt.plot(covid_timeline.index, covid_timeline.values, label='COVID Trials', marker='o')
plt.plot(breast_cancer_timeline.index, breast_cancer_timeline.values, label='Breast Cancer Trials', marker='o')

plt.xlabel('Timeline (Two-Month Periods)')
plt.ylabel('Number of Trials')
plt.title('Clinical Trials Timeline Comparison')
plt.legend()
plt.show()