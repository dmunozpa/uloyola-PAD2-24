

list = []

list.append("7")
list.append("56")
list.append("78")

##################
# ITERATE OVER A LIST 
##################
for value in list:
    print(f"Element: {value}")

################
# CHECK A VALUE IN LIST 
################
if "7" in list:
    print("Exist")
else:
    print("Dont exist")


################
# CHECK A VALUE IN LIST AND THIS VALUE IS UNIQUE
################
value = "7"
if value not in list:
    list.append(value)

