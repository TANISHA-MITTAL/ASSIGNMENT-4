for TotalCandies in range(200):
    if (TotalCandies % 5 != 2):
        continue
    if (TotalCandies % 6 != 3):
        continue
    if (TotalCandies % 7 != 2):
        continue

    print(str(TotalCandies) + " candies are in the bowl!")
    break