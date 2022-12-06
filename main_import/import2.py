# from imports import import1

# print(list(import1.calculate(2)),import1.add(2,3),import1.sub(2,3))


# from imports import *

# print(import1.add(2,3),import1.sub(5,3))
# import3.import3()

# os.mkdir('test')
# types of imports
# help("modules") for more modules 
from dateutil import relativedelta
from datetime import date,datetime

now = datetime.now()
today_date = date.today()
jobs = [
    {
        'title':'Python Developer',
        'company' : 'Google',
        'location' : 'Mountain View, CA',
        'date_posted' : '2020-05-10',
        'description' : 'Python Dev with 5+ years of exp',
        'salary' : 100000,
    },
    {
        'title' : 'Java Developer',
        'company' : 'Facebook',
        'location' : 'Menlo Park CA',
        'date_posted' : '2022-12-5',
        'description' : 'Java Developer with 5+ years of exp',
        'salary' : 200000,
    },    
    {
        'title' : 'PHP Developer',
        'company' : 'Instagram',
        'location' : 'Hoolicon CA',
        'date_posted' : '2021-12-5',
        'description' : 'Php Developer with 6+ years of exp',
        'salary' : 200000,
    }
]
def check_job_validity():
    print()
    for job_index in range(len(jobs)):
        val = jobs[job_index]['date_posted'].split('-')
        val = jobs[job_index]['date_posted'].split('-')
        if date(int(val[0]),int(val[1]),int(val[2])) < today_date :
            diff = relativedelta.relativedelta(today_date,date(int(val[0]),int(val[1]),int(val[2])))
            print(f'{jobs[job_index]["title"]} position for {jobs[job_index]["company"]} has expired {diff.years} years,{diff.months} months,{diff.days} days ago.')
        else:
            print(f'Job is valid for {jobs[job_index]["title"]} position in {jobs[job_index]["company"]}')
    print()

check_job_validity()





