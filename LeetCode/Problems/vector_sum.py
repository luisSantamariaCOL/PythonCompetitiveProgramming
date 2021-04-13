def vectorsum(vector1, vector2):
    sum = []
    for i in range(len(vector1)):
            sum.append(vector1[i]+vector2[i])
    return sum


vector1 = [1,2,3,4]
vector2 = [5,6,7,8]

print(vector1)
print(vector2)
print(vectorsum(vector1, vector2))