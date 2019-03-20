# stuents = ['Jane', 'Alam', 'Parag', 'Nihal', 'Johny']
# for positon in range(len(stuents)):
#     print(stuents[positon])



ages =[ 30, 40, 50, 60, 70,100]
maxNumber = max(ages)

print('Top Number: '+ str(maxNumber))

for positon in range(len(ages)):
    if maxNumber == ages[positon]:
        ages.remove(ages[positon])

print('Second Top: '+str(max(ages)))



