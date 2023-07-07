from src.utils import *


def test_split_dataframe_by_percentage():
    hr_data = read_excel_file('hr_data.xlsx')
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
    split_dataframe_by_percentages(percentages_labels, hr_data)
    write_excel_file(hr_data, 'test_hr_output.xlsx')

