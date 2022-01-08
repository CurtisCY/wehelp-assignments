def avg(data):

    employeesNumber = data['count']
    sum=0
    for employee in data['employees']:
        #print(employee)
        #print(type(employee))
        #print(employee['salary'])
        sum = sum + employee['salary']

    print("員工人數", employeesNumber)
    print("員工薪資總和", sum)
    print("員工平均薪資", sum/employeesNumber)

avg({
        "count":3,
        "employees":[
            {
                "name":"John",
                "salary": 30000
            },
            {
                "name":"Bob",
                "salary":60000
            },
            {
                "name":"Jenny",
                "salary":50000
            }
        ]
})