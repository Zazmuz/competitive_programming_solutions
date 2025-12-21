month, date, year = input().split("/")
months = ["januar", "februar", "marts", "april", "maj", "juni", "juli", "august", "september", "oktober", "november", "december"]
print(f"{int(date)}. {months[int(month)-1]} {year}")