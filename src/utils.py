import datetime
import pandas as pd
import math
import random
import math


def read_configuration_files():
    hr_raw_data = read_excel_file('MBA_Stats_Project_Lab_03_07_2023.xlsx')
    contract_types = read_excel_file('contract_type_data_configuration.xlsx')
    departments_percentages = read_excel_file('departments_percentages_labels.xlsx')


def init_data():
    """for index, contract_type in contract_types.iterrows():
        value = math.ceil((contract_type["Percentage"] / 100) * len(hr_data.index))
        for i in range(value):
            index = random.randint(1, len(hr_data.index))
            while(True):
                if index in assigned_indecies:
                    index = random.randint(1, len(hr_data.index))
                else:
                    break
            hr_data.at[index, 'Contract Type'] = contract_type["Code"]
            assigned_indecies.append(index)"""

    #hr_data = convert_list_of_dictionaries_to_dataframe(assign_number_of_promotions(hr_data))

    """
    employees_with_education_levels = assign_employees_education_levels(hr_data)
    hr_data = convert_list_of_dictionaries_to_dataframe(employees_with_education_levels)"""
    write_excel_file(hr_raw_data, 'MBA_Stats_Project_Lab_03_07_2023_Output.xlsx')


def assign_working_hours(hr_raw_data):
    """
    Assign working hours based on contract type
    :param hr_raw_data:
    :return:
    """


def assign_contract_type(hr_raw_data):
    """
    Assign contract type
    :param hr_raw_data:
    :return:
    """


def get_graduated_year(age):
    years_since_graduation = age - 22
    current_year = int(datetime.datetime.now().date().strftime("%Y-%m-%d").split('-')[0])
    return current_year - years_since_graduation


def get_joining_date():
    current_year, current_month, current_day = datetime.datetime.now().date().strftime("%Y-%m-%d").split('-')
    current_year = int(current_year)
    current_month = int(current_month)
    current_day = int(current_day)
    new_year = random.randint(current_year, current_year - 40)
    new_month = random.randint(current_month, 1) if new_year == current_year else random.randint(1, 12)
    new_day = random.randint(current_day, 1) if new_month == current_month else random.randint(1, 30)
    return f"""{str(new_year)}-{str(new_month).zfill(2)}-{str(new_day).zfill(2)}"""


def data_cleaning():
    hr_data = read_excel_file('MBA_Stats_Project_Lab_03_07_2023_Output_V12.xlsx')
    hr_data['Contract type'] = hr_data.apply(lambda x: 3)
    #
    #hr_data['Branch'] = hr_data.apply(lambda x: random.choice(branches), axis=1)
    performance = {
        'Poor': 5,
        'Below': 20,
        'Good': 50,
        'Very good': 20,
        'Excellent': 5
    }
    write_excel_file(hr_data, 'MBA_Stats_Project_Lab_03_07_2023_Output_V13.xlsx')


def split_female_male(fullName):
    females = [
        'Salma', 'Heidi', 'Roya', 'Naglaa', 'Lamees',
        'Laila', 'Afaf', 'Lelian', 'Wafaa', 'Menna', 'Mervat', 'Doaa',
        'Roqya'
    ]
    return 'F' if fullName.split(' ')[0] in females else 'M'


def get_age(birth_year):
    current_year, current_month, current_day = datetime.datetime.now().date().strftime("%Y-%m-%d").split('-')
    current_year = int(current_year)
    return current_year - birth_year


def construct_name():
    first_names = ['Ahmed', 'Mohamed', 'Gamal', 'Nasser',
                   'Salma', 'Islam', 'Heidi', 'Roya', 'Naglaa', 'Lamees',
                   'Laila', 'Afaf', 'Lelian', 'Wafaa', 'Menna', 'Mervat', 'Doaa',
                   'Aziz', 'Adham', 'Hesham', 'Salah', 'Roqya', 'Morad',
                   'Fayed', 'Omar', 'Adam', 'Hashem', 'Ali', 'Hadi', 'Soliman']
    last_names = ['Ahmed', 'Mohamed', 'Gamal', 'Nasser',
                  'Islam', 'Adham', 'Hesham', 'Salah',
                  'Morad', 'Fayed', 'Ashraf', 'Omar', 'Adam', 'Hashem', 'Ali', 'Hadi', 'Soliman']
    return random.choice(first_names) + " " + random.choice(last_names)


def split_dataframe_by_percentages(percentages_labels: dict, dataframe: pd.DataFrame, column: str):
    first_index = 0
    for percentage_label in percentages_labels.keys():
        percentage_value = math.ceil((percentages_labels[percentage_label] / 100) * len(dataframe.index))
        last_index = percentage_value + first_index
        dataframe.loc[first_index:last_index, column] = percentage_label
        first_index = last_index


def assign_direct_manager():
    hr_data = read_excel_file('hr_output.xlsx')
    departments = hr_data["Department"].unique()
    grades = hr_data["Grade"].unique()
    for department in departments:
        for grade in grades:
            employees_grades = hr_data.query('Department == @department and Grade == @grade')
            employees_grades_len = len(employees_grades.index)
            grade_manager = grade + 1
            employees_grades_managers = hr_data.query('Department == @department and Grade == @grade_manager')
            employees_grades_managers_len = len(employees_grades_managers.index)
            if employees_grades_managers_len < employees_grades_len:
                print("Department : " + department)


def get_employees_grade(number_of_promotions):
    employees_grades_mapping = {0: (1, 2),
                                1: (3, 4),
                                2: (5, 6),
                                3: (7,)}
    for key in employees_grades_mapping.keys():
        if number_of_promotions in employees_grades_mapping[key]:
            return key


def get_renewal_date():
    current_year, current_month, current_day = datetime.datetime.now().date().strftime("%Y-%m-%d").split('-')
    current_year = int(current_year)
    current_month = int(current_month)
    current_day = int(current_day)
    new_year = random.randint(current_year, current_year + 3)
    new_month = random.randint(current_month, 12) if new_year == current_year else random.randint(1, 12)
    new_day = random.randint(current_day, 30) if new_month == current_month else random.randint(1, 30)
    return f"""{str(new_year)}-{str(new_month).zfill(2)}-{str(new_day).zfill(2)}"""


def get_current_salary(grade):
    if math.isnan(grade):
        grade = 0

    grades_salaries = {
        0: (10000, 12000),
        1: (12000, 17000),
        2: (17000, 20000),
        3: (20000, 25000)
    }
    return random.randint(grades_salaries[grade][0], grades_salaries[grade][1])


def convert_list_of_dictionaries_to_dataframe(dict_list):
    return pd.DataFrame(dict_list)


def assign_number_of_promotions(hr_data):
    number_of_promotions_percentages = {
        1: 25,
        2: 25,
        3: 20,
        4: 15,
        5: 10,
        6: 2,
        7: 3
    }
    departments = hr_data["Department"].unique()
    employees_with_promotions = []
    for department_name in departments:
        department_employees = hr_data.loc[hr_data["Department"] == department_name]
        number_of_employees = len(department_employees.index)
        department_employees = department_employees.to_dict('records')
        last_index = 0
        for promotion_percentage in number_of_promotions_percentages.keys():
            value = math.ceil((number_of_promotions_percentages[promotion_percentage] / 100) * number_of_employees)
            print(value)
            if value > 0 and value > last_index:
                for employee_promotion in department_employees[last_index:value]:
                    employee_promotion["Number of promotions"] = promotion_percentage
            last_index = value

        employees_with_promotions.extend(department_employees)
    write_excel_file(convert_list_of_dictionaries_to_dataframe(employees_with_promotions))
    return employees_with_promotions


def assign_employees_education_levels(data):
    departments = data["Department"].unique()
    education_levels = read_excel_file('education_level_data_configuration.xlsx')
    employees_with_education_levels = []
    for department_name in departments:
        department_employees = data.loc[data["Department"] == department_name]
        number_of_employees = len(department_employees.index)
        departments_education_levels = education_levels.loc[education_levels["Percentage"] != 0]. \
            loc[education_levels["Department"] == department_name].to_dict('records')
        department_employees = department_employees.to_dict('records')
        last_index = 0
        for department_education_level in departments_education_levels:
            value = math.ceil((department_education_level["Percentage"] / 100) * number_of_employees)
            for employee_education_level in department_employees[last_index:value]:
                employee_education_level["Education Level"] = department_education_level["Education Level"]
            last_index = value
        employees_with_education_levels.extend(department_employees)
    return employees_with_education_levels


def write_excel_file(dataframe, file_name='hr_output.xlsx'):
    dataframe.to_excel(file_name, index=False)


def read_excel_file(file_name):
    return pd.read_excel('./files/' + file_name)