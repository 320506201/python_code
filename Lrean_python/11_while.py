temp = [[1,36.6],[2,35.5],[3,34.4],[4,33.3],[5,38.9],[6,37.8],[7,36.7],[8,35.6],[9,34.5],[10,33.4],[11,40]]
i = 0
print("hi")
while i < len(temp):
    a = temp[i]
    if a[1] >= 37:
        print (a[0] , "," , a[1])
    i += 1
print("above 37")