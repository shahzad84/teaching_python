# when you wanna store key value pair we should use dictionaries
#NOTE: key should be unique

customer={
    "name":"shahzad",
    "age":23,
    "is_varified":True

}
customer["name"]="me"#reassign new name
customer["data"]=2#passing new key and value
# print(customer["name"])
print(customer.get("name", "good"))#good is default value

# .get if we use .get it will not throw weird error when we don't pass anything.
