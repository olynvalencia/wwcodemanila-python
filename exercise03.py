careers = ['programmer', 'driver', 'cook', 'teacher']

# Get the index of 'teacher'
print(careers.index('teacher'))

# Check if 'teacher' is in the careers list
print('teacher' in careers)

careers.append('athlete')
careers.insert(1, 'baker')
for car in careers:
    print(car)