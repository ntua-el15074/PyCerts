string = "Percentage spent by category \n"
catperc = [{"name" : "Food", "Percentage" : 45, "listofos" : []},{"name" : "Auto", "Percentage" : 60, "listofos" : []},{"name" : "Clothing", "Percentage" : 20, "listofos" : []}]
percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

for i in range(0, len(catperc)):
    for j in range(0, len(percentages)):
        if catperc[i]["Percentage"] > percentages[j]:
            catperc[i]["listofos"].append("0")
        else:
            catperc[i]["listofos"].append(" ")

for item in range(0, len(percentages)):
    string = string + f"{percentages[item]:>3}|"#  + " " + catperc[0]["listofos"][item] + " " + catperc[1]["listofos"][item] + " " + catperc[2]["listofos"][item] + "\n"
    for jitem in range(0, len(catperc)):
        string = string + " " + catperc[jitem]["listofos"][item]
    string = string + "\n"
string = string + "    ----------"

maximum = catperc[0]["name"]
for k in range(0, len(catperc)):
    if len(catperc[k]["name"]) > len(maximum):
        maximum = catperc[k]["name"]

print(maximum)


for i in ["string", "booldozer"]:
    for k in range(max(len("string"), len("booldozer"))):
        string = string + i[k]

# for i in catperc:
#     for k in i["name"]:
#         print(catperc[i]["name"][k])

print(string)

