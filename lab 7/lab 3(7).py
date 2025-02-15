employee=[
    {"dept no":"100","roll no":"1","salary":"55000"},
    {"dept no":"101","roll no":"2","salary":"100000"},
    {"dept no":"100","roll no":"3","salary":"70000"},
    {"dept no":"103","roll no":"4","salary":"75000"},
    {"dept no":"103","roll no":"5","salary":"80000"},
    {"dept no":"101","roll no":"6","salary":"90000"},
]

for emp in employee:
    emp["salary"] = int(emp["salary"])

for emp in employee:
    for other_emp in employee:
        if emp != other_emp and emp["dept no"] == other_emp["dept no"]:
            if emp["salary"] > other_emp["salary"]:
                print(f"{emp} has a higher salary than {other_emp}")