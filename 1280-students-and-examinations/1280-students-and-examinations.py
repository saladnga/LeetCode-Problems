import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross = students.merge(subjects, how='cross').sort_values(by=['student_id', 'subject_name'])
    count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    res = cross.merge(count, how='left', on=['student_id', 'subject_name'])
    res['attended_exams'] = res['attended_exams'].fillna(0)
    return res