#Task_5_6
pupils = [
 {
'firstname': 'Masha',
 'Group': 42,
 'physics': 7,
 'informatics': 6,
 'history': 8,
 },
 {
  'firstname': 'Misha',
 'Group': 42,
 'physics': 4,
 'informatics': 3,
 'history': 2,   
 },
 {
 'firstname': 'Dasha',
 'Group': 42,
 'physics': 8,
 'informatics': 10,
 'history': 7,
 }
]

for i in pupils:
    average_score = (i['physics'] + i['informatics'] + i['history']) / 3
    if average_score >4:
        print (i['firstname'])


