def pair(filename):
    
    file = open(r"/home/pr7/Desktop/FlaskTryFirst/data/test_pairs.txt","w")
    L=[filename+' '+'002980_1.jpg'+"\n",
       filename+' '+'003311_1.jpg'+"\n",
       filename+' '+'003376_1.jpg'+"\n",
       filename+' '+'003852_1.jpg'+"\n",
       filename+' '+'004285_1.jpg'+"\n",
       filename+' '+'004795_1.jpg'+"\n",
       filename+' '+'008266_1.jpg'+"\n",
       filename+' '+'008681_1.jpg'+"\n",
       filename+' '+'009790_1.jpg']
    file.writelines(L)
    