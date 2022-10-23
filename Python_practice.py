counties = ["Arapahoe" , "Denver" , "Jefferson"]

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#Using for to print counties
for county in counties:
    print(county)

#Using range to print counties
for i in range(len(counties)):
    print(counties[i])

