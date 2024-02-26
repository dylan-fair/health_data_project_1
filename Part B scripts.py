import pandas as pd
import matplotlib.pyplot as plt

breast_cancer = pd.read_csv('BreastCancer.csv')
covid = pd.read_csv('COVID.csv')

# study status
bc_status_count = breast_cancer['Study Status'].value_counts()
covid_status_count = covid['Study Status'].value_counts()

bc_status_percent = bc_status_count / bc_status_count.sum() * 100
covid_status_percent = covid_status_count / covid_status_count.sum() * 100

status_comparison = pd.DataFrame({
    'Breast Cancer': bc_status_percent,
    'COVID': covid_status_percent})

status_comparison.plot(kind='bar', figsize=(14, 7), width=0.8)
plt.title('Comparison of Study Status between Breast Cancer and COVID')
plt.ylabel('Status Percentage')
plt.xlabel('Study Status')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# study results
bc_results_count = breast_cancer['Study Results'].value_counts()
plt.figure(figsize=(8, 8))
bc_results_count.plot.pie(autopct='%1.1f%%', colors=['lightgrey', 'lightgreen'])
plt.title('Study Results in Breast Cancer')
plt.ylabel('')
plt.show()

covid_results_count = covid['Study Results'].value_counts()
plt.figure(figsize=(8, 8))
covid_results_count.plot.pie(autopct='%1.1f%%', colors=['lightgrey', 'lightgreen'])
plt.title('Study Results in COVID')
plt.ylabel('')
plt.show()

# intervention type
def intervention_type(intervention):
    interventions = intervention.split('|')
    types = set([i.split(':')[0].strip().capitalize() for i in interventions])
    return ', '.join(sorted(types))

breast_cancer['Intervention Types'] = breast_cancer['Interventions'].apply(intervention_type)
covid['Intervention Types'] = covid['Interventions'].apply(intervention_type)

bc_intervention_type = breast_cancer.assign(Types=breast_cancer['Intervention Types'].str.split(', ')).explode('Types')
covid_intervention_type = covid.assign(Types=covid['Intervention Types'].str.split(', ')).explode('Types')

bc_type_count = bc_intervention_type['Types'].value_counts()
bc_type_percent = bc_type_count / bc_type_count.sum() * 100

covid_type_count = covid_intervention_type['Types'].value_counts()
covid_type_percent = covid_type_count / covid_type_count.sum() * 100

intervention_type_comparison = pd.DataFrame({
    'Breast Cancer': bc_type_percent,
    'COVID': covid_type_percent})

intervention_type_comparison.plot(kind='bar', figsize=(12, 9), width=0.8)
plt.title('Comparison of Intervention Type between Breast Cancer and COVID')
plt.ylabel('Type Percentage')
plt.xlabel('Intervention Types')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# sex
bc_sex_count = breast_cancer['Sex'].value_counts()
plt.figure(figsize=(8, 8))
bc_sex_count.plot.pie(autopct='%1.1f%%', pctdistance=0.90, colors=['lightgrey', 'lightgreen', 'orange'])
plt.title('Sex Distribution in Breast Cancer')
plt.ylabel('')
plt.show()

covid_sex_count = covid['Sex'].value_counts()
plt.figure(figsize=(8, 8))
covid_sex_count.plot.pie(autopct='%1.1f%%', pctdistance=0.90, colors=['lightgrey', 'lightgreen', 'orange'])
plt.title('Sex Distribution in COVID')
plt.ylabel('')
plt.show()

# age
bc_age = breast_cancer.assign(AgeGroup=breast_cancer['Age'].str.split(', ')).explode('AgeGroup')
covid_age = covid.assign(AgeGroup=covid['Age'].str.split(', ')).explode('AgeGroup')

bc_age_count = bc_age['AgeGroup'].value_counts()
bc_age_percent = bc_age_count / bc_age_count.sum() * 100

covid_age_count = covid_age['AgeGroup'].value_counts()
covid_age_percent = covid_age_count / covid_age_count.sum() * 100

age_comparison = pd.DataFrame({
    'Breast Cancer': bc_age_percent,
    'COVID': covid_age_percent})

age_comparison.plot(kind='bar', width=0.8)
plt.title('Comparison of Age Group between Breast Cancer and COVID')
plt.ylabel('Age Group Percentage')
plt.xlabel('Age Group')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# phase
bc_phase = breast_cancer.assign(Phase=breast_cancer['Phases'].str.split('|')).explode('Phase')
covid_phase = covid.assign(Phase=covid['Phases'].str.split('|')).explode('Phase')

bc_phase_count = bc_phase['Phase'].value_counts()
bc_phase_percent = bc_phase_count / bc_phase_count.sum() * 100

covid_phase_count = covid_phase['Phase'].value_counts()
covid_phase_percent = covid_phase_count / covid_phase_count.sum() * 100

phase_comparison = pd.DataFrame({
    'Breast Cancer': bc_phase_percent,
    'COVID': covid_phase_percent})

phase_comparison.plot(kind='bar', width=0.8)
plt.title('Comparison of Phase between Breast Cancer and COVID')
plt.ylabel('Phase Percentage')
plt.xlabel('Phase')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# enrollment
def categorize_enrollment(enrollment):
    if enrollment <= 10:
        return '0-10'
    elif enrollment <= 50:
        return '11-50'
    elif enrollment <= 100:
        return '51-100'
    elif enrollment <= 1000:
        return '101-1000'
    else:
        return '>1000'

breast_cancer['Enrollment Category'] = breast_cancer['Enrollment'].apply(categorize_enrollment)
covid['Enrollment Category'] = covid['Enrollment'].apply(categorize_enrollment)

bc_enrollment_count = breast_cancer['Enrollment Category'].value_counts()
bc_enrollment_percent = bc_enrollment_count / bc_enrollment_count.sum() * 100

covid_enrollment_count = covid['Enrollment Category'].value_counts()
covid_enrollment_percent = covid_enrollment_count / covid_enrollment_count.sum() * 100

enrollment_comparison = pd.DataFrame({
    'Breast Cancer': bc_enrollment_percent,
    'COVID': covid_enrollment_percent})

category_order = ['0-10', '11-50', '51-100', '101-1000', '>1000']
enrollment_comparison = enrollment_comparison.reindex(category_order)

enrollment_comparison.plot(kind='bar', figsize=(12, 9), width=0.8)
plt.title('Comparison of Enrollment Category between Breast Cancer and COVID')
plt.ylabel('Enrollment Category Percentage')
plt.xlabel('Enrollment Category')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# funder type
bc_funder_count = breast_cancer['Funder Type'].value_counts()
bc_funder_percent = bc_funder_count / bc_funder_count.sum() * 100

covid_funder_count = covid['Funder Type'].value_counts()
covid_funder_percent = covid_funder_count / covid_funder_count.sum() * 100

funder_comparison = pd.DataFrame({
    'Breast Cancer': bc_funder_percent,
    'COVID': covid_funder_percent})

funder_comparison.plot(kind='bar', figsize=(10, 10), width=0.8)
plt.title('Comparison of Funder Type between Breast Cancer and COVID')
plt.ylabel('Funder Type Percentage')
plt.xlabel('Funder Type')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# study design
def study_design_split(design):
    design_details = design.split('|')
    types = [i.split(':')[1].strip().upper() for i in design_details]
    return types

breast_cancer['new_column'] = breast_cancer['Study Design'].apply(study_design_split)
covid['new_column'] = covid['Study Design'].apply(study_design_split)

def study_design(df):
    allocation = []
    intervention_model = []
    masking = []
    primary_purpose = []

    for i in df['new_column']:
        allocation.append(i[0])
        intervention_model.append(i[1])
        masking.append(i[2])
        primary_purpose.append(i[3])

    study_design_df = pd.DataFrame({
        'Allocation': allocation,
        'Intervention Model': intervention_model,
        'Masking': masking,
        'Primary Purpose': primary_purpose
    })

    return study_design_df

bc_study_design_df = study_design(breast_cancer)
bc_study_design_df = bc_study_design_df[bc_study_design_df['Allocation'] != '']
covid_study_design_df = study_design(covid)

def masking_select(type):
    type = type.split('(')
    return type[0]

bc_study_design_df['Masking'] = bc_study_design_df['Masking'].apply(masking_select)
covid_study_design_df['Masking'] = covid_study_design_df['Masking'].apply(masking_select)

for i in ['Allocation', 'Intervention Model', 'Masking', 'Primary Purpose']:
    bc_count = bc_study_design_df[i].value_counts()
    bc_percent = bc_count / bc_count.sum() * 100

    covid_count = covid_study_design_df[i].value_counts()
    covid_percent = covid_count / covid_count.sum() * 100

    study_design_comparison = pd.DataFrame({'Breast Cancer': bc_percent, 'COVID': covid_percent})
    study_design_comparison.plot(kind='barh', figsize=(9, 7), width=0.8)
    plt.title(f'Comparison of {i} between Breast Cancer and COVID')
    plt.xlabel(f'{i} Percentage')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

# study duration
breast_cancer['Start Date'] = pd.to_datetime(breast_cancer['Start Date'])
breast_cancer['Completion Date'] = pd.to_datetime(breast_cancer['Completion Date'])
breast_cancer['Study Duration'] = breast_cancer['Completion Date'] - breast_cancer['Start Date']
breast_cancer['Study Duration'] = breast_cancer['Study Duration'].dt.days

covid['Start Date'] = pd.to_datetime(covid['Start Date'])
covid['Completion Date'] = pd.to_datetime(covid['Completion Date'])
covid['Study Duration'] = covid['Completion Date'] - covid['Start Date']
covid['Study Duration'] = covid['Study Duration'].dt.days

def categorize_duration(duration):
    if duration <= 120:
        return '0-120'
    elif duration <= 360:
        return '121-360'
    elif duration <= 600:
        return '361-600'
    elif duration <= 1000:
        return '601-1000'
    else:
        return '>1000'

breast_cancer['Duration Category'] = breast_cancer['Study Duration'].apply(categorize_duration)
covid['Duration Category'] = covid['Study Duration'].apply(categorize_duration)

bc_duration_count = breast_cancer['Duration Category'].value_counts()
bc_duration_percent = bc_duration_count  / bc_duration_count.sum() * 100

covid_duration_count = covid['Duration Category'].value_counts()
covid_duration_percent = covid_duration_count / covid_duration_count.sum() * 100

duration_comparison = pd.DataFrame({
    'Breast Cancer': bc_duration_percent,
    'COVID': covid_duration_percent})

category_order = ['0-120', '121-360', '361-600', '601-1000', '>1000']
duration_comparison = duration_comparison.reindex(category_order)

duration_comparison.plot(kind='bar', figsize=(10, 7), width=0.8)
plt.title('Comparison of Study Duration Category between Breast Cancer and COVID')
plt.ylabel('Study Duration Category Percentage')
plt.xlabel('Study Duration Category')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


