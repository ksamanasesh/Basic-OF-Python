import pandas as pa

a = [1,2,3,4]
b = pa.Series(a)
print("Series :\n",b)

data = pa.DataFrame({"CSK":["Dhoni","Jadeja","Ruturaj"],"RCB":["Kholi","Maxwell","FAf"],"GT":["Pandya","Gill","Rashid"]})
print(data)

table = pa.read_csv("D:\\Python\\Files Analysing\\Filescv.csv")
print("Table :\n",table)


print("Locating :\n",table.loc[2][3])                        # First index rows next Column

data1 = {
    "MI":["Rohit","Ishan","Sky"],
    "CSK":["Dhoni","Rahane","Jadeja"],
    "GT":["Pandya","Gill","Rashid"],
    "RCB":["Virat","Faf","Maxwell"]
}
data2 = {
    "RR":["Buttler","Ashwin","Chahal"],
    "DC":["Warner","shaw","Axar"],
    "LSG":["Rahul","Pooran","Avesh"],
    "KKR":["Rinku","Iyer","Rana"]
}

team1 = pa.DataFrame(data1)
team2 = pa.DataFrame(data2)

IPL = pa.concat([team1,team2],axis=1)
print("Concat :\n",IPL)

dtt = pa.DataFrame()
dtt = pa.date_range("2/4/2023",periods=10,freq="10H")

print(dtt)
