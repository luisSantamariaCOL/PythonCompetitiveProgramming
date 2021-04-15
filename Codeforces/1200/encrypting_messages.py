def sum_mssg(message, encryption, i):
    for j in range(len(encryption)):
        message[i+j] = message[i+j] + encryption[j]
    return message

n, m, c = input().split()
n = int(n)
m = int(m)
c = int(c)

message = input().split()
message = [int(i) for i in message]


encryption = input().split()
encryption = [int(i) for i in encryption]

for i in range(n-m+1):
   message = sum_mssg(message, encryption, i)

for i in range(len(message)):
    message[i] %= c

print(" ".join([str(x) for x in message]))
