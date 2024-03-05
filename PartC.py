import pandas as pd
import matplotlib.pyplot as plt
import json

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

top_15 = sorted(covid_drugs.items(), key=lambda x: x[1], reverse=True)[:15]

drugs, counts = zip(*top_15)

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.barh(drugs, counts, color='skyblue')
plt.xlabel('Number of Studies')
plt.title('Top 15 Drugs Studied Under COVID')
plt.gca().invert_yaxis()  
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

breast_cancer_filtered = breast_cancer[(breast_cancer['Start Date'] >= '2020-01-01') | (breast_cancer['Start Date_month'] >= '2020-01-01')]

breast_cancer_filtered.drop(columns=['Start Date_month'], inplace=True)

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


# Read JSON file
with open("covidEvents.json", "r") as file:
    data = json.load(file)

term_counts = {}
for entry in data:
    if "resultsSection" in entry:
        adverse_events_module = entry.get("resultsSection", {}).get("adverseEventsModule", {})
        if "seriousEvents" in adverse_events_module:
            serious_events = adverse_events_module["seriousEvents"]
            for event in serious_events:
                term = event.get("term", "")
                if term:
                    term_counts[term] = term_counts.get(term, 0) + 1

# Get top 10 terms
top_terms = sorted(term_counts.items(), key=lambda x: x[1], reverse=True)[:10]
terms, counts = zip(*top_terms)

# Create graph
plt.bar(terms, counts)
plt.xlabel('Terms')
plt.ylabel('Occurrences')
plt.title('Top 10 Adverse Events for Covid-19')
plt.xticks(rotation=45, ha="right")
plt.show()

with open("breastCancerEvents.json", "r") as file:
    data = json.load(file)

term_counts = {}
for entry in data:
    if "resultsSection" in entry:
        adverse_events_module = entry.get("resultsSection", {}).get("adverseEventsModule", {})
        if "seriousEvents" in adverse_events_module:
            serious_events = adverse_events_module["seriousEvents"]
            for event in serious_events:
                term = event.get("term", "")
                if term:
                    term_counts[term] = term_counts.get(term, 0) + 1

top_terms = sorted(term_counts.items(), key=lambda x: x[1], reverse=True)[:10]

terms, counts = zip(*top_terms)

# Create graph
plt.bar(terms, counts)
plt.xlabel('Terms')
plt.ylabel('Occurrences')
plt.title('Top 10 Adverse Events for Breast Cancer')
plt.xticks(rotation=45, ha="right")
plt.show()