#! /usr/bin/python3

#list_to_add = ['']
#list_item = input('Enter a word to be added to the list (or quit to end):')
#while len(list_to_add) != 0:
#    list_to_add.append(list_item)
#    if list_item == 'quit':
#        print(list_to_add[1::2])
#        break
#    else:
#        list_item = input('Enter a word to be added to the list (or stop to end):')
#print(list_to_add[2::2])

word_list = []

while True:
    word = input('Please enter a word (type quit to stop):')
    if word == 'quit':
        break
    word_list.append(word)
print(word_list[::2])
print(word_list[1::2])