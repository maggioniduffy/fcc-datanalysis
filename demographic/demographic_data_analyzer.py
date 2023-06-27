import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./adult.data.csv')
    print(df.head())
    
    TOTAL_ROWS = len(df.index)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df['race'].unique().tolist()
    data = {}
    for r in races:
        count = len(df[df['race']==r])
        data[r] = count
    race_count = pd.Series(data=data, index=races)
    
    # What is the average age of men?
    men_rows = df[df['sex']=='Male']
    men_ages = men_rows['age']
    average_age_men = men_ages.mean()
    average_age_men = round(average_age_men,1)
    
    # What is the percentage of people who have a Bachelor's degree?
    total_bachelors = len(df[df['education']=='Bachelors'])
    
    percentage_bachelors = round(total_bachelors/TOTAL_ROWS * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    advanced_education = df[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')]
    advanced_education_totals = len(advanced_education.index)
    advanced_education_50k = advanced_education[advanced_education['salary'] == '>50K']
    advanced_education_50k_totals = len(advanced_education_50k.index)
    
    lower_education = df[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]
    lower_education_totals = len(lower_education.index)
    lower_education_50k = lower_education[lower_education['salary'] == '>50K']
    lower_education_50k_totals = len(lower_education_50k.index)
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = 
    # lower_education = None

    # percentage with salary >50K
    higher_education_rich = round(advanced_education_50k_totals/advanced_education_totals * 100,1)
    lower_education_rich = round(lower_education_50k_totals/lower_education_totals * 100,1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary']=='>50K')]
    num_min_workers = len(min_workers.index)
    rich_percentage = num_min_workers/TOTAL_ROWS*100
    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].unique().tolist()
    highest_earning_country = None
    highest_earning_country_percentage = 0
    
    for c in countries:
        country = df[df['native-country']==c]
        totals = len(country.index)
        country_richs = country[country['salary']=='>50K']
        country_richs = len(country_richs.index)
        country_perc = round(country_richs/totals * 100,1)
        if (country_perc > highest_earning_country_percentage):
            highest_earning_country_percentage = country_perc
            highest_earning_country = c

    # Identify the most popular occupation for those who earn >50K in India.
    india_50k = df[(df['native-country']=='India')&(df['salary']=='>50K')]
    indian_ocuppations = india_50k['occupation'].unique().tolist()
    top_IN_occupation = None
    top_q_occupation = 0
    for i in indian_ocuppations:
        aux = india_50k[india_50k['occupation']==i]
        count = len(aux)
        if (count > top_q_occupation):
            top_IN_occupation = i
            top_q_occupation = count
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
