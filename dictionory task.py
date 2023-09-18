doctor ={
    "title": "specialist",
    "name": "baburam",
    "EmploymentYear": 2005
}
print(doctor)
doctor["gender"] = "male"

def print_doctor_details(doctor_info):
    Title = doctor_info["title"]
    name = doctor_info["name"]
    year = doctor_info["EmploymentYear"]
    gender = doctor_info["gender"]

    formatted_info = (f"title: {Title} and name: {name} year: {year} gender:{gender}")
    print(formatted_info)

print(print_doctor_details(doctor))


