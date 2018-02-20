def edit_distance(word1,word2):
 
    length1 = len(word1)
    length2 = len(word2)
    k = [0]

    columns = []

    for x in range(0,length1+2):

            if (x == 0):
                columns.append('0')
                k.append('0')

            elif (x < length1+1):
                columns.append(str(x-1))
                k.append(word1[x-1])

            else:
                columns.append(str(x-1))
   


    columns = [columns]
    columns = [k] + columns


    for y in range(0,(length2)):
        
        current= []

            
        for x in range(0,length1+2):

            if (x == 0):
                current.append(word2[y])

            elif (x == 1):
                current.append((y+1))

            else:

                if (word1[x-2] == word2[y]):
                    diagonal = int(columns[y+1][x-1])
                    
                    current.append(diagonal)


                else:
                    top = int(columns[y+1][x]) + 1
                    left = int(current[x-1]) + 1
                    diagonal = int(columns[y+1][x-1]) + 1


                    current.append(min(top,left,diagonal)) 


        columns = columns + [current]


    return columns[-1][-1]




def spellcheck(word,library):
    #the parameter library represents a predetermined list of words
    
    
    length1= len(word)

    first_choice = []

    for x in library:
        length2 = len(x)

        if ((length2 == length1) or (length2 == (length1-1)) or (length2 == (length1+1))):
            first_choice.append(x)

    
    #deleting stuff so they wont appear in later choices

    library = [x for x in library if x not in first_choice]

    second_choice = []

    for x in library:
        length3 = len(x)

        if (length3 == length1-2) or (length3 == length1+2):
            second_choice.append(x)
            
    
    library = [x for x in library if x not in second_choice]

    third_choice = []

    for x in library:
        length4 = len(x)

        if (length4 == length1-3) or (length4 == length1+3):
            third_choice.append(x)

    
    library = [x for x in library if x not in third_choice]
    
    #output operations, edit distance checkers

    output = []
    

    for x in first_choice:

        if (edit_distance(word,x) == 1):
            output.append(x)


    first_choice = [x for x in first_choice if x not in output]


    while (1 == 1):


        if (output ==[]):
            break


        print("Did you mean")
        print(output) 

        r = input()


        if (r == "yes"):
            print("Sucess!")
            return

        else:
            break


    output = []
    second_choice = second_choice + first_choice


    for x in second_choice:

        if (edit_distance(word,x) == 2):
            output.append(x)


    second_choice = [x for x in second_choice if x not in output]


    while (1 == 1):


        if (output ==[]):
            break


        print("Did you mean")
        print(output)

        r = input()

        
        if (r == "yes"):
            print("Sucess!")
            return

        else:
            break



    output = []
    third_choice = third_choice + second_choice


    for x in third_choice:

        if (edit_distance(word,x) == 3):
            output.append(x)


    while (1 == 1):
        

        if (output ==[]):
            print("Sorry, No Words left!")
            return


        print("Did you mean")
        print(output)

        r = input()


        if (r == "yes"):
            print("Sucess!")
            return

        else:
            print("Sorry, No Words left!")
            return



allword = open("morewords.txt","r")

loword = [line.split(',') and line.replace("\n","") for line in allword.readlines()]


a = input()

spellcheck(a,loword)







