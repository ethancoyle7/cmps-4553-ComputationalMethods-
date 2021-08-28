import datetime#gather the current date from inport
 
print(" I am going to calculate your age now \n\n")

Birth_Year = int(input("Enter the year you were born: \n"))
Birth_Month = int(input("Enter the month you were born: \n"))
Birth_Day = int(input("Enter the day you were born: \n"))
 
CurrYear = datetime.date.today().year
CurrMonth = datetime.date.today().month
CurrDay = datetime.date.today().day
 
years = CurrYear - Birth_Year
months = abs(CurrMonth-Birth_Month)#cannot be negative months
days = abs(CurrDay-Birth_Day)#no negative days dont make no sense

print("You Are : ", years, "Years old ", months, " months and", days, "days old \n")
print("You are Also:  ", years*31536000+months*2592000+days*86400,
"seconds old \n")
