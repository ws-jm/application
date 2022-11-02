listway = {
 'Madurai': ['Cochin', 'Kanyakumari'],
 'Vaishali': [],
 'Varanasi': ['Khajuraho', 'Bodhgaya'],
 'Thiruvanandhapuram': ['Kanyakumari'],
 'Udaipur': ['Gir', 'Ajanta'],
 'Rishikesh': ['Delhi'],
 'Shimla': ['Rishikesh'],
 'Bangalore': ['Chennai', 'Madurai'],
 'Agra': ['Ranthambore'],
 'Ellora': ['Aurangabad'],
 'Bodhgaya': ['Kolkatta'],
 'Cochin': ['Thiruvanandhapuram'],
 'Pushkar': ['Udaipur', 'Ranthambore'],
 'Ranthambore': ['Khajuraho'],
 'Gir': [],
 'Aurangabad': ['Mumbai'],
 'Kolkatta': ['Ajanta', 'Bangalore', 'Chennai'],
 'Chennai': ['Madurai'],
 'Sravasti': ['Kushinagar'],
 'Leh': ['Shimla'],
 'Sarnath': ['Varanasi'],
 'Delhi': ['Jaipur', 'Agra', 'Sravasti'],
 'Goa': ['Cochin', 'Bangalore'],
 'Kanyakumari': [],
 'Kushinagar': ['Sarnath', 'Vaishali'],
 'Khajuraho': ['Ajanta'],
 'Jaipur': ['Pushkar'],
 'Mumbai': ['Goa'],
 'Ajanta': ['Ellora', 'Aurangabad']
}

def findCity(cur_c_index):
 if len(listway[listKey[cur_c_index]]) == 0:
  if len(avaibleWay) > len(MaxWay) - 1:
   MaxWay.clear()
   MaxWay.insert(0,listKey[key_re])
   for j in avaibleWay:
    MaxWay.append(j)
   return
 for i in listway[listKey[cur_c_index]]:
  avaibleWay.append(i)
  findCity(listKey.index(i))
  avaibleWay.pop()
 
listKey = list(listway.keys())

avaibleWay = []
MaxWay = []

key_re = 0
for i in listKey:
 findCity(key_re)
 key_re += 1

print(MaxWay)
