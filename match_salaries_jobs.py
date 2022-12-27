def match(candidate, job):
    try:
        if candidate['min_salary']*0.9 <= job['max_salary']:
            return True
        else:
            return False
    except:
        return 'Error'

candidate1 = {'min_salary': 120000}
candidate2 = {'min_salary': 190000}
job1 = {'max_salary': 130000}
job2 = {'max_salary': 80000}
job3 = {'max_salary': 171000}
print(match(candidate1, job1))
print(match(candidate1, job2))
print(match(candidate1, job3))
print(match(candidate2, job1))
print(match(candidate2, job2))
print(match(candidate2, job3))