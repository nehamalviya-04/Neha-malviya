
```python
import pandas as pd
df=pd.read_csv("ds_salaries.csv")
print(df.head)
```

    <bound method NDFrame.head of      Unnamed: 0  work_year experience_level employment_type  \
    0             0       2020               MI              FT   
    1             1       2020               SE              FT   
    2             2       2020               SE              FT   
    3             3       2020               MI              FT   
    4             4       2020               SE              FT   
    ..          ...        ...              ...             ...   
    602         602       2022               SE              FT   
    603         603       2022               SE              FT   
    604         604       2022               SE              FT   
    605         605       2022               SE              FT   
    606         606       2022               MI              FT   
    
                          job_title  salary salary_currency  salary_in_usd  \
    0                Data Scientist   70000             EUR          79833   
    1    Machine Learning Scientist  260000             USD         260000   
    2             Big Data Engineer   85000             GBP         109024   
    3          Product Data Analyst   20000             USD          20000   
    4     Machine Learning Engineer  150000             USD         150000   
    ..                          ...     ...             ...            ...   
    602               Data Engineer  154000             USD         154000   
    603               Data Engineer  126000             USD         126000   
    604                Data Analyst  129000             USD         129000   
    605                Data Analyst  150000             USD         150000   
    606                AI Scientist  200000             USD         200000   
    
        employee_residence  remote_ratio company_location company_size  
    0                   DE             0               DE            L  
    1                   JP             0               JP            S  
    2                   GB            50               GB            M  
    3                   HN             0               HN            S  
    4                   US            50               US            L  
    ..                 ...           ...              ...          ...  
    602                 US           100               US            M  
    603                 US           100               US            M  
    604                 US             0               US            M  
    605                 US           100               US            M  
    606                 IN           100               US            L  
    
    [607 rows x 12 columns]>
    


```python
import pandas as pd

def describe_dataframe(df):
    # Get all column names
    print("Column Names:")
    for col in df.columns:
        print(f"- {col}")

    print("\nColumn Descriptions:\n")
    for col in df.columns:
        print(f"Column: {col}")
        print(f"Data Type: {df[col].dtype}")
        print(f"Number of Missing Values: {df[col].isnull().sum()}")

        if pd.api.types.is_numeric_dtype(df[col]):
            # If column is numeric, use describe() for summary stats
            print(df[col].describe())
        else:
            # If column is non-numeric, show unique values and count
            unique_vals = df[col].unique()
            print(f"Number of Unique Values: {len(unique_vals)}")
            print(f"Sample Unique Values: {unique_vals[:5]}")  # Show first 5 unique values

        print("-" * 40)

# Example usage
# Assuming df is your DataFrame
describe_dataframe(df)

```

    Column Names:
    - Unnamed: 0
    - work_year
    - experience_level
    - employment_type
    - job_title
    - salary
    - salary_currency
    - salary_in_usd
    - employee_residence
    - remote_ratio
    - company_location
    - company_size
    
    Column Descriptions:
    
    Column: Unnamed: 0
    Data Type: int64
    Number of Missing Values: 0
    count    607.000000
    mean     303.000000
    std      175.370085
    min        0.000000
    25%      151.500000
    50%      303.000000
    75%      454.500000
    max      606.000000
    Name: Unnamed: 0, dtype: float64
    ----------------------------------------
    Column: work_year
    Data Type: int64
    Number of Missing Values: 0
    count     607.000000
    mean     2021.405272
    std         0.692133
    min      2020.000000
    25%      2021.000000
    50%      2022.000000
    75%      2022.000000
    max      2022.000000
    Name: work_year, dtype: float64
    ----------------------------------------
    Column: experience_level
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 4
    Sample Unique Values: ['MI' 'SE' 'EN' 'EX']
    ----------------------------------------
    Column: employment_type
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 4
    Sample Unique Values: ['FT' 'CT' 'PT' 'FL']
    ----------------------------------------
    Column: job_title
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 50
    Sample Unique Values: ['Data Scientist' 'Machine Learning Scientist' 'Big Data Engineer'
     'Product Data Analyst' 'Machine Learning Engineer']
    ----------------------------------------
    Column: salary
    Data Type: int64
    Number of Missing Values: 0
    count    6.070000e+02
    mean     3.240001e+05
    std      1.544357e+06
    min      4.000000e+03
    25%      7.000000e+04
    50%      1.150000e+05
    75%      1.650000e+05
    max      3.040000e+07
    Name: salary, dtype: float64
    ----------------------------------------
    Column: salary_currency
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 17
    Sample Unique Values: ['EUR' 'USD' 'GBP' 'HUF' 'INR']
    ----------------------------------------
    Column: salary_in_usd
    Data Type: int64
    Number of Missing Values: 0
    count       607.000000
    mean     112297.869852
    std       70957.259411
    min        2859.000000
    25%       62726.000000
    50%      101570.000000
    75%      150000.000000
    max      600000.000000
    Name: salary_in_usd, dtype: float64
    ----------------------------------------
    Column: employee_residence
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 57
    Sample Unique Values: ['DE' 'JP' 'GB' 'HN' 'US']
    ----------------------------------------
    Column: remote_ratio
    Data Type: int64
    Number of Missing Values: 0
    count    607.00000
    mean      70.92257
    std       40.70913
    min        0.00000
    25%       50.00000
    50%      100.00000
    75%      100.00000
    max      100.00000
    Name: remote_ratio, dtype: float64
    ----------------------------------------
    Column: company_location
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 50
    Sample Unique Values: ['DE' 'JP' 'GB' 'HN' 'US']
    ----------------------------------------
    Column: company_size
    Data Type: object
    Number of Missing Values: 0
    Number of Unique Values: 3
    Sample Unique Values: ['L' 'S' 'M']
    ----------------------------------------
    


```python
unique_Jobs_posts = df['job_title'].unique()
print(unique_Jobs_posts)
unique_locations = df['company_location'].unique()
print(unique_locations)


```

    ['Data Scientist' 'Machine Learning Scientist' 'Big Data Engineer'
     'Product Data Analyst' 'Machine Learning Engineer' 'Data Analyst'
     'Lead Data Scientist' 'Business Data Analyst' 'Lead Data Engineer'
     'Lead Data Analyst' 'Data Engineer' 'Data Science Consultant'
     'BI Data Analyst' 'Director of Data Science' 'Research Scientist'
     'Machine Learning Manager' 'Data Engineering Manager'
     'Machine Learning Infrastructure Engineer' 'ML Engineer' 'AI Scientist'
     'Computer Vision Engineer' 'Principal Data Scientist'
     'Data Science Manager' 'Head of Data' '3D Computer Vision Researcher'
     'Data Analytics Engineer' 'Applied Data Scientist'
     'Marketing Data Analyst' 'Cloud Data Engineer' 'Financial Data Analyst'
     'Computer Vision Software Engineer' 'Director of Data Engineering'
     'Data Science Engineer' 'Principal Data Engineer'
     'Machine Learning Developer' 'Applied Machine Learning Scientist'
     'Data Analytics Manager' 'Head of Data Science' 'Data Specialist'
     'Data Architect' 'Finance Data Analyst' 'Principal Data Analyst'
     'Big Data Architect' 'Staff Data Scientist' 'Analytics Engineer'
     'ETL Developer' 'Head of Machine Learning' 'NLP Engineer'
     'Lead Machine Learning Engineer' 'Data Analytics Lead']
    ['DE' 'JP' 'GB' 'HN' 'US' 'HU' 'NZ' 'FR' 'IN' 'PK' 'CN' 'GR' 'AE' 'NL'
     'MX' 'CA' 'AT' 'NG' 'ES' 'PT' 'DK' 'IT' 'HR' 'LU' 'PL' 'SG' 'RO' 'IQ'
     'BR' 'BE' 'UA' 'IL' 'RU' 'MT' 'CL' 'IR' 'CO' 'MD' 'KE' 'SI' 'CH' 'VN'
     'AS' 'TR' 'CZ' 'DZ' 'EE' 'MY' 'AU' 'IE']
    


```python
country_full_names = {
    'DE': 'Germany', 'JP': 'Japan', 'GB': 'United Kingdom', 'HN': 'Honduras', 'US': 'United States',
    'HU': 'Hungary', 'NZ': 'New Zealand', 'FR': 'France', 'IN': 'India', 'PK': 'Pakistan',
    'CN': 'China', 'GR': 'Greece', 'AE': 'United Arab Emirates', 'NL': 'Netherlands', 'MX': 'Mexico',
    'CA': 'Canada', 'AT': 'Austria', 'NG': 'Nigeria', 'ES': 'Spain', 'PT': 'Portugal',
    'DK': 'Denmark', 'IT': 'Italy', 'HR': 'Croatia', 'LU': 'Luxembourg', 'PL': 'Poland',
    'SG': 'Singapore', 'RO': 'Romania', 'IQ': 'Iraq', 'BR': 'Brazil', 'BE': 'Belgium',
    'UA': 'Ukraine', 'IL': 'Israel', 'RU': 'Russia', 'MT': 'Malta', 'CL': 'Chile',
    'IR': 'Iran', 'CO': 'Colombia', 'MD': 'Moldova', 'KE': 'Kenya', 'SI': 'Slovenia',
    'CH': 'Switzerland', 'VN': 'Vietnam', 'AS': 'American Samoa', 'TR': 'Turkey', 'CZ': 'Czech Republic',
    'DZ': 'Algeria', 'EE': 'Estonia', 'MY': 'Malaysia', 'AU': 'Australia', 'IE': 'Ireland'
}

# Replace country codes with full names
df['company_location'] = df['company_location'].replace(country_full_names)
df['employee_residence'] = df['employee_residence'].replace(country_full_names)
print(df)
```

         Unnamed: 0  work_year experience_level employment_type  \
    0             0       2020               MI              FT   
    1             1       2020               SE              FT   
    2             2       2020               SE              FT   
    3             3       2020               MI              FT   
    4             4       2020               SE              FT   
    ..          ...        ...              ...             ...   
    602         602       2022               SE              FT   
    603         603       2022               SE              FT   
    604         604       2022               SE              FT   
    605         605       2022               SE              FT   
    606         606       2022               MI              FT   
    
                          job_title  salary salary_currency  salary_in_usd  \
    0                Data Scientist   70000             EUR          79833   
    1    Machine Learning Scientist  260000             USD         260000   
    2             Big Data Engineer   85000             GBP         109024   
    3          Product Data Analyst   20000             USD          20000   
    4     Machine Learning Engineer  150000             USD         150000   
    ..                          ...     ...             ...            ...   
    602               Data Engineer  154000             USD         154000   
    603               Data Engineer  126000             USD         126000   
    604                Data Analyst  129000             USD         129000   
    605                Data Analyst  150000             USD         150000   
    606                AI Scientist  200000             USD         200000   
    
        employee_residence  remote_ratio company_location company_size  
    0              Germany             0          Germany            L  
    1                Japan             0            Japan            S  
    2       United Kingdom            50   United Kingdom            M  
    3             Honduras             0         Honduras            S  
    4        United States            50    United States            L  
    ..                 ...           ...              ...          ...  
    602      United States           100    United States            M  
    603      United States           100    United States            M  
    604      United States             0    United States            M  
    605      United States           100    United States            M  
    606              India           100    United States            L  
    
    [607 rows x 12 columns]
    


```python
company_resize = {
    'L': 'Large_Scale', 'S': 'Small_Scale', 'M': 'Midium_Scale', 
}
df['company_size'] = df['company_size'].replace(company_resize)
print(df)
```

         Unnamed: 0  work_year experience_level employment_type  \
    0             0       2020               MI              FT   
    1             1       2020               SE              FT   
    2             2       2020               SE              FT   
    3             3       2020               MI              FT   
    4             4       2020               SE              FT   
    ..          ...        ...              ...             ...   
    602         602       2022               SE              FT   
    603         603       2022               SE              FT   
    604         604       2022               SE              FT   
    605         605       2022               SE              FT   
    606         606       2022               MI              FT   
    
                          job_title  salary salary_currency  salary_in_usd  \
    0                Data Scientist   70000             EUR          79833   
    1    Machine Learning Scientist  260000             USD         260000   
    2             Big Data Engineer   85000             GBP         109024   
    3          Product Data Analyst   20000             USD          20000   
    4     Machine Learning Engineer  150000             USD         150000   
    ..                          ...     ...             ...            ...   
    602               Data Engineer  154000             USD         154000   
    603               Data Engineer  126000             USD         126000   
    604                Data Analyst  129000             USD         129000   
    605                Data Analyst  150000             USD         150000   
    606                AI Scientist  200000             USD         200000   
    
        employee_residence  remote_ratio company_location  company_size  
    0              Germany             0          Germany   Large_Scale  
    1                Japan             0            Japan   Small_Scale  
    2       United Kingdom            50   United Kingdom  Midium_Scale  
    3             Honduras             0         Honduras   Small_Scale  
    4        United States            50    United States   Large_Scale  
    ..                 ...           ...              ...           ...  
    602      United States           100    United States  Midium_Scale  
    603      United States           100    United States  Midium_Scale  
    604      United States             0    United States  Midium_Scale  
    605      United States           100    United States  Midium_Scale  
    606              India           100    United States   Large_Scale  
    
    [607 rows x 12 columns]
    


```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
average_salary_by_country = df.groupby('company_location')['salary_in_usd'].mean().round(2)
top10company = average_salary_by_country.sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top10company.index, y=top10company.values, palette='viridis')
plt.xlabel('Company Location')
plt.ylabel('Average Salary in USD')
plt.title('Top 10 High-Paying Country by Average Salary')
plt.xticks(rotation=45)
plt.show()
job_title_counts = df['job_title'].value_counts()

print(job_title_counts)
df['job_title_counts'] = df['job_title'].map(df['job_title'].value_counts())

print(df)
```


    
![png](output_6_0.png)
    


    job_title
    Data Scientist                              143
    Data Engineer                               132
    Data Analyst                                 97
    Machine Learning Engineer                    41
    Research Scientist                           16
    Data Science Manager                         12
    Data Architect                               11
    Big Data Engineer                             8
    Machine Learning Scientist                    8
    Principal Data Scientist                      7
    AI Scientist                                  7
    Data Science Consultant                       7
    Director of Data Science                      7
    Data Analytics Manager                        7
    ML Engineer                                   6
    Computer Vision Engineer                      6
    BI Data Analyst                               6
    Lead Data Engineer                            6
    Data Engineering Manager                      5
    Business Data Analyst                         5
    Head of Data                                  5
    Applied Data Scientist                        5
    Applied Machine Learning Scientist            4
    Head of Data Science                          4
    Analytics Engineer                            4
    Data Analytics Engineer                       4
    Machine Learning Developer                    3
    Machine Learning Infrastructure Engineer      3
    Lead Data Scientist                           3
    Computer Vision Software Engineer             3
    Lead Data Analyst                             3
    Data Science Engineer                         3
    Principal Data Engineer                       3
    Principal Data Analyst                        2
    ETL Developer                                 2
    Product Data Analyst                          2
    Director of Data Engineering                  2
    Financial Data Analyst                        2
    Cloud Data Engineer                           2
    Lead Machine Learning Engineer                1
    NLP Engineer                                  1
    Head of Machine Learning                      1
    3D Computer Vision Researcher                 1
    Data Specialist                               1
    Staff Data Scientist                          1
    Big Data Architect                            1
    Finance Data Analyst                          1
    Marketing Data Analyst                        1
    Machine Learning Manager                      1
    Data Analytics Lead                           1
    Name: count, dtype: int64
         Unnamed: 0  work_year experience_level employment_type  \
    0             0       2020               MI              FT   
    1             1       2020               SE              FT   
    2             2       2020               SE              FT   
    3             3       2020               MI              FT   
    4             4       2020               SE              FT   
    ..          ...        ...              ...             ...   
    602         602       2022               SE              FT   
    603         603       2022               SE              FT   
    604         604       2022               SE              FT   
    605         605       2022               SE              FT   
    606         606       2022               MI              FT   
    
                          job_title  salary salary_currency  salary_in_usd  \
    0                Data Scientist   70000             EUR          79833   
    1    Machine Learning Scientist  260000             USD         260000   
    2             Big Data Engineer   85000             GBP         109024   
    3          Product Data Analyst   20000             USD          20000   
    4     Machine Learning Engineer  150000             USD         150000   
    ..                          ...     ...             ...            ...   
    602               Data Engineer  154000             USD         154000   
    603               Data Engineer  126000             USD         126000   
    604                Data Analyst  129000             USD         129000   
    605                Data Analyst  150000             USD         150000   
    606                AI Scientist  200000             USD         200000   
    
        employee_residence  remote_ratio company_location  company_size  \
    0              Germany             0          Germany   Large_Scale   
    1                Japan             0            Japan   Small_Scale   
    2       United Kingdom            50   United Kingdom  Midium_Scale   
    3             Honduras             0         Honduras   Small_Scale   
    4        United States            50    United States   Large_Scale   
    ..                 ...           ...              ...           ...   
    602      United States           100    United States  Midium_Scale   
    603      United States           100    United States  Midium_Scale   
    604      United States             0    United States  Midium_Scale   
    605      United States           100    United States  Midium_Scale   
    606              India           100    United States   Large_Scale   
    
         job_title_counts  
    0                 143  
    1                   8  
    2                   8  
    3                   2  
    4                  41  
    ..                ...  
    602               132  
    603               132  
    604                97  
    605                97  
    606                 7  
    
    [607 rows x 13 columns]
    


```python
# Step 1: Aggregate the total counts for each job title
total_counts = df.groupby('job_title')['job_title_counts'].sum().nlargest(5)

# Step 2: Filter original DataFrame to include only the top 5 job titles
top5_df = df[df['job_title'].isin(total_counts.index)]

# Step 3: Create a pivot table for plotting
df_pivot = top5_df.pivot_table(index='job_title', columns='remote_ratio', values='job_title_counts', aggfunc='sum').fillna(0)

# Define colors for each remote_ratio
colors = {0: 'blue', 50: 'orange', 100: 'red'}

# Plot the stacked bar chart
df_pivot.plot(kind='bar', stacked=True, color=[colors[r] for r in df_pivot.columns], figsize=(10, 6))

# Customizing the plot to match your style
plt.title('Top 5 Job Titles by Distribution of Remote Ratio')
plt.xlabel('Job Title')
plt.ylabel('Count of Job Title')
plt.xticks(rotation=45, ha='right')
plt.legend(title='remote_ratio', labels=[0, 50, 100], loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()
```


    
![png](output_7_0.png)
    



```python
company_count= df['company_size'].value_counts()
print(company_count)
plt.pie(company_count,labels=company_count.index, autopct='%1.1f%%',colors=sns.color_palette("viridis",len(company_count)))
plt.title("Proportion of Company Names")
plt.show()
```

    company_size
    Midium_Scale    326
    Large_Scale     198
    Small_Scale      83
    Name: count, dtype: int64
    


    
![png](output_8_1.png)
    



```python
experience_count= df['experience_level'].value_counts()
print(experience_count)
plt.pie(experience_count,labels=experience_count.index, autopct='%1.1f%%',colors=sns.color_palette("Paired",len(experience_count)))
plt.title("Proportion of Company Names")
plt.show()


```

    experience_level
    SE    280
    MI    213
    EN     88
    EX     26
    Name: count, dtype: int64
    


    
![png](output_9_1.png)
    



```python
import pandas as pd

# Sample function to look up information for a specific country
def country_lookup(df, country_name):
    # Filter the DataFrame for the specified country
    country_data = df[df['company_location'] == country_name]

    # Check if there is any data for the specified country
    if country_data.empty:
        return f"No data available for {country_name}."
    
    # Display relevant information for the specified country
    print(f"Information for companies in {country_name}:\n")
    for index, row in country_data.iterrows():
        print(f"Work Year: {row['work_year']}")
        print(f"Experience Level: {row['experience_level']}")
        print(f"Employment Type: {row['employment_type']}")
        print(f"Job Title: {row['job_title']}")
        print(f"Salary: {row['salary']} {row['salary_currency']}")
        print(f"Salary in USD: ${row['salary_in_usd']}")
        print(f"Employee Residence: {row['employee_residence']}")
        print(f"Remote Ratio: {row['remote_ratio']}")
        print(f"Company Location: {row['company_location']}")
        print(f"Company Size: {row['company_size']}")
        print(f"Job Title Counts: {row['job_title_counts']}")
        print("-" * 40)  # Separator for readability

# Example usage
country_lookup(df, "Russia")
 
```

    Information for companies in Russia:
    
    Work Year: 2021
    Experience Level: EX
    Employment Type: FT
    Job Title: Head of Data
    Salary: 230000 USD
    Salary in USD: $230000
    Employee Residence: Russia
    Remote Ratio: 50
    Company Location: Russia
    Company Size: Large_Scale
    Job Title Counts: 5
    ----------------------------------------
    Work Year: 2021
    Experience Level: EX
    Employment Type: FT
    Job Title: Head of Data Science
    Salary: 85000 USD
    Salary in USD: $85000
    Employee Residence: Russia
    Remote Ratio: 0
    Company Location: Russia
    Company Size: Midium_Scale
    Job Title Counts: 4
    ----------------------------------------
    
**My insights** 
In the dataset 14.5% members are freshers while most quota is filled by Senior Engineers at 46.1%.
During the period 2020-2022, 62.8% of members have shifted to work from home modalities owing to Covid - 19 crisis. Later, we will see trend shifting back to the normalcy.
It can be observed that Data Scientist is the most common job title followed by Data Engineers and Data Analysts respectively.
US accounted for 63.97% of Count of employee residence.
At 332, US had the highest Count of employee residence and was 5,433.33% higher than BR, which had the lowest Count of employee residence at 6.

```python

```


```python

```
