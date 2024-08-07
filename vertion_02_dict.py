# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student Name: W.A.K.D.Tharuka
# Date: 2023/04/20

## Declaration of variables
status="y"
student_id=""
Pass=0
Defer=0
Fail=0
Total=0
progression_outcome=0
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0
Total_outcomes=0
Main_List1=[] # Student ID
Main_List2=[] # Pass , Defer , Fail values
Main_List3=[] # progression outcomes
progression_dict={}
ID=0
x=0
y=0


# Defined function to find progression outcome
def progression(Pass,Defer,Fail):

    if Pass==120:
        progression_outcome="Progress"   
    elif Pass==100:
        progression_outcome="Progress (module trailer)"   
    elif Pass<=80 and Fail<=60:
        progression_outcome="Module retriever"  
    else:
        progression_outcome="Exclude"

    print(progression_outcome)
    # To get the "progression_outcome" out of the progression function, use the command ".var" and assign it to the variable "progression.var"
    progression.var=progression_outcome


# Defined function to display Histogram
def Histogram(progress_count,trailer_count,retriever_count,exclude_count):

    ## Declaration of Lists
    progression_outcome_list=["Progress ","Trailer  ","Retriever","Excluded "]
    progression_count=[progress_count,trailer_count,retriever_count,exclude_count]

    print("------------------------------------------------------------")
    print("Histogram")

    i=0 ## Indexing variable
    for progression_outcome in progression_outcome_list:
        star=""
        # Assigning each "progression outcome" count from the list named "progression_count" to a variable named "x"
        for x in range(progression_count[i]):
            star+="* "
        print(progression_outcome,progression_count[i],":",star)
        i+=1

    # Adding the "progression outcome" count        
    Total_outcomes=progress_count+trailer_count+retriever_count+exclude_count
    print()
    print(Total_outcomes,"outcome/s in total.")
    print("------------------------------------------------------------")


### .............. Part 1 - Main Version ..............


# Asking whether the user wants to continue in the program or quit and handling the loop accordingly
# Assigning the user's answer to the variable "status"    
while status=="y":

    ## Declaration of Lists
    List1=[] # Student ID
    List2=[] # Pass , Defer , Fail values
    volume_credit_num=[0,20,40,60,80,100,120]

    # Student ID No. validity check
    while True:
        try:
            student_id=str(input("Please enter your Student ID No. : "))
        
        except ValueError:
            print("Student ID required.")
            print()
            continue

        else:
            if student_id[0]=="w" and len(student_id)==8:
                # Part 4
                # Appending the Student ID entered by the user to the list named "List1"
                List1.append(student_id)
                print()
                break
            else:
                print(".... Enter a valid student ID No. ....")
                print("# Please enter your student ID No. as per the format below")
                print("# Must be a 7-digit student number starting with a simple 'w'")
                print("  Ex. w1234567 ")
                print()
                continue

    # Pass credit level validity check
    while True:
        try:
            Pass=int(input("Please enter your credits at pass : "))

        except ValueError:
            print("Integer required.")
            print()
            continue

        else:
            if Pass in volume_credit_num:
                # Part 4
                # Appending the Credit value entered by the user to the list named "List2"
                List2.append(Pass)
                break
            else:
                print("Out of range.")
                print("# You can only enter the following credit levels.")
                print(volume_credit_num)
                print()
                continue
    
    # Defer credit level validity check
    while True:
        try:
            Defer=int(input("Please enter your credits at defer : "))

        except ValueError:
            print("Integer required.")
            print()
            continue

        else:
            if Defer in volume_credit_num:
                # Part 4
                # Appending the Credit value entered by the user to the list named "List2"
                List2.append(Defer)
                break
            else:
                print("Out of range.")
                print("# You can only enter the following credit levels.")
                print(volume_credit_num)
                print()
                continue

    # Fail credit level validity check
    while True:
        try:
            Fail=int(input("Please enter your credits at fail : "))

        except ValueError:
            print("Integer required.")
            print()
            continue

        else:
            if Fail in volume_credit_num:
                # Part 4
                # Appending the Credit value entered by the user to the list named "List2"
                List2.append(Fail)
                break
            else:
                print("Out of range.")
                print("# You can only enter the following credit levels.")
                print(volume_credit_num)
                print()
                continue

    # checking the total of credit level
    Total=Pass+Defer+Fail
    if Total==120:
        
        # Calling the progression function
        progression(Pass,Defer,Fail)

        # Counting the progression outcome
        if progression.var=="Progress":
            progress_count+=1
        elif progression.var=="Progress (module trailer)":
            trailer_count+=1
        elif progression.var=="Module retriever":
            retriever_count+=1
        else:
            exclude_count+=1

        # Part 4
        # Append the list named "List1" to the list named "Main_List1"
        Main_List1.append(List1)
        # Append the list named "List2" to the list named "Main_List2"
        Main_List2.append(List2)
        # Append the list called "Main_List3" to the "progression.var" found by the progression function
        Main_List3.append(progression.var)

    else:
        print("Total incorrect.")
        print("# Try Again !!")
        
    # Asking if the user wants to continue or quit the program
    print("\nWould you like to enter another set of data?")
    while True:
        status=input("Enter 'y' for yes or 'q' to quit and view results : ")
        if status!="y" and status!="q":
            print(".... Enter correct command ....\n")     
        else:
            print()
            break

# Calling the Histogram function
Histogram(progress_count,trailer_count,retriever_count,exclude_count)


### .............. End of the Part 1 ..............


### .............. Part 4 - Dictionary ..............

print("\nPart 4:")

# Entering data into the dictionary
n=0 ## Indexing variable
for ID in Main_List1:
    # Enter key and value elements from "Main_List1" , "Main_List2" , "Main_List3" lists into the "progression_dict" dictionary
    progression_dict[ID[0]]=Main_List3[n]+" - "+str(Main_List2[n][0])+", "+str(Main_List2[n][1])+", "+str(Main_List2[n][2])
    n+=1

# Display the data in the dictionary (key as x , value as y)
for x,y in progression_dict.items():
    print(x,":",y)

print()

### .............. End of the Part 4 ..............

