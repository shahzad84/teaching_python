# student_grade={
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Eva": 88
# }

# for name,grade in student_grade.items():
#     print(f"{name} scored {grade} marks. ")


# second question

phone =input("phone : ")
digits_mapping={
    "1":"one",
    "2":"Two",
    "3":"third"
}

output=""
for ch in phone:
    output+=digits_mapping.get(ch, "!")+ " "
print(output)
