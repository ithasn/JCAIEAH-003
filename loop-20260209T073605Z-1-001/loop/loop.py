stars = ''
size = 5

for i in range(size) :
    for j in range(1 + i) :
        stars += '* '
    stars += '\n'

print(stars)

# result => * 
#           * *
#           * * *
#           * * * *
#           * * * * *
