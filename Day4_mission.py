#8.2

dic ={
    "dog" : "chien",
    "cat" : "chat,",
    "walrus" : "morse"
}
new_dic={}
for key,value in dic.items():
    new_dic[value] = key

print(new_dic["chien"])