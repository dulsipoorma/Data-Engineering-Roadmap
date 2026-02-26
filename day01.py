tech_stack=["Python", "SQL", "PostgreSQL"]

my_profile={
    "name":"Dulsi",
    "role":"Aspiring Data engineer",
    "skills":tech_stack
            }

print("Hi, I'm", my_profile["name"])
print("My goal is to be a ",my_profile["role"])
print("I am learning ",my_profile["skills"])

tech_stack.append("cloud")
print("Updated skills ",my_profile["skills"])
