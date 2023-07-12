"""
Fill data file contains the essentials for creating the final Excel file with a complete dataset
"""
from src.utils import *

"""
1- Read configration files
2- Fill personal data
3- Fill job data
"""


def fill_personal_information(hr_raw_data):
    """
    Personal information like Name, Gender, Date of birth, Year of birth, Smoker, PWD
    :return:
    """
    zones = ['Qatamya', 'Sheikh zayed', 'Tagamo', 'Maadi', 'Nasr City',
             'Masr El-Gedida', 'Imbaba', 'Feisel', 'Benha',
             'Tanta', 'Sedi Beshr', 'Agamy', 'Miami', 'Smoha',
             'El-Anfoshy', 'Zezeneia', 'Kafr Abdo']

    hr_raw_data['name'] = hr_raw_data.apply(lambda x: construct_name(), axis=1)
    hr_raw_data['date_of_birth'] = hr_raw_data['Date of birth'].astype(str)
    hr_raw_data['year_of_birth'] = hr_raw_data.apply(lambda x: x['Date of birth'].split('-')[0], axis=1)
    hr_raw_data['smoker'] = hr_raw_data.apply(lambda x: random.randint(0, 1), axis=1)
    hr_raw_data['pwd'] = hr_raw_data.apply(lambda x: 0, axis=1)
    pwd_rows = math.ceil((5 / 100) * len(hr_raw_data.index))
    for i in range(pwd_rows):
        hr_raw_data.at[random.randint(1, len(hr_raw_data.index)), 'pwd'] = 1
    hr_raw_data['gender'] = hr_raw_data.apply(lambda x: split_female_male(x['name']), axis=1)
    hr_raw_data['age'] = hr_raw_data.apply(lambda x: get_age(x['year_of_birth']), axis=1)
    hr_raw_data['zone'] = hr_raw_data.apply(lambda x: random.choice(zones), axis=1)


def fill_job_data(hr_raw_data):
    """
    Job data is any data related to the job: working hours, contract_type,
    current_salary, contract_renewal_date, contract_renewal_year, caffein_intake
    :param hr_raw_data:
    :return:
    """
    percentages_labels = {
        'HR': 2,
        'Marketing': 2,
        'BezDev': 2,
        'Sales': 6,
        'Admin_And_Facilities': 4,
        'Legal': 1,
        'Product_Management': 10,
        'IT_Support': 21,
        'R_And_D': 22,
        'Engineering': 25,
        'Training': 2,
        'Finance': 3,
    }
    hr_raw_data['graduation_year'] = hr_raw_data.apply(lambda x: get_graduated_year(x['Age']), axis=1)
    hr_raw_data['years_experience'] = hr_raw_data.apply(lambda x: int(datetime.datetime.now().date().strftime("%Y-%m-%d").split('-')[0]) - x['graduation_year'], axis=1)
    hr_raw_data['joining_date'] = hr_raw_data.apply(lambda x: get_joining_date(), axis=1)
    hr_raw_data['contract_renewal_date'] = hr_raw_data.apply(lambda x: get_renewal_date(), axis=1)
    hr_raw_data['contract_renewal_year'] = hr_raw_data.apply(lambda x: x['contract_renewal_year'].split('-')[0], axis=1)
    hr_raw_data['current_salary'] = hr_raw_data.apply(lambda x: get_current_salary(x['Grade']), axis=1)
    hr_raw_data['caffeine_intake'] = hr_raw_data.apply(lambda x: random.randint(1, 10), axis=1)
    split_dataframe_by_percentages(percentages_labels, hr_raw_data, 'Department')