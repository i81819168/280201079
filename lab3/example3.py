month=str(input("month(e.g. january):"))
day=int(input("day:"))

if month in ("april","may","june"):
  season="spring"
elif month in ("july","august","september"):
  season="summer"
elif month in ("october","november","december"):
  season="fall"
elif month in ("january","february","march"):
  season="winter"


if month == "march" and day>=20:
  season="spring"
elif month == "june" and day>=21:
  season="summer"
elif month == "september" and day>=22:
  season="fall"
elif month == "december" and day>=21:
  season="winter"

print("season is:",season)
