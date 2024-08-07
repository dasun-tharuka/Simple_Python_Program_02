# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student Name: W.A.K.D.Tharuka
# Date: 2023/04/20

## Declaration of variables
user=""
status="y"
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
Main_List1=[] # Pass , Defer , Fail values
Main_List2=[] # progression outcomes
Text_file=0


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
            # Adding "* " each to the variable named "star"
            star+="* "             
        print(progression_outcome,progression_count[i],":",star)
        i+=1

    # Adding the "progression outcome" count
    Total_outcomes=progress_count+trailer_count+retriever_count+exclude_count
    print()
    print(Total_outcomes,"outcome/s in total.")
    print("------------------------------------------------------------")
    
# Asking if the user is a student as "s" or a staff member as "m"
# Student - Displaying only progress outcomes and Histogram
# Staff member - Displaying progression outcomes, Histogram, part 2 - List, and Part 3 - Text file
print("Are you a student or staff member?")
while True:
    user=input("Enter 's' for student or 'm' to staff member : ")
    if user!="s" and user!="m":
        print("....Enter correct command....\n")   
    else:
        print()
        break

### .............. Part 1 - Main Version ..............


# Asking whether the user wants to continue in the program or quit and handling the loop accordingly
# Assigning the user's answer to the variable "status"
while status=="y":

    ## Declaration of Lists
    List1=[] # Pass , Defer , Fail values
    volume_credit_num=[0,20,40,60,80,100,120]

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
                # Part 2 - List
                # Appending the Credit value entered by the user to the list named "List1"
                List1.append(Pass)
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
                # Part 2 - List
                # Appending the Credit value entered by the user to the list named "List1"
                List1.append(Defer)
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
                # Part 2 - List
                # Appending the Credit value entered by the user to the list named "List1"
                List1.append(Fail)
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

        # Part 2 - List
        # Append the list named "List1" to the list named "Main_List1"
        Main_List1.append(List1)
        # Append the list called "Main_List2" to the "progression.var" found by the progression function
        Main_List2.append(progression.var)

    else:
        print("Total incorrect.")
    
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

# Check if the user is a staff member as "m"
if user=="m":
    
### .............. Part 2 – List ..............

    print("\nPart 2:")
    
    # Display the "progression_outcome","pass","defer","fail" in "Main_List1" and "Main_List2" lists properly to the user
    n=0 ## Indexing variable
    for progression_outcome in Main_List2:
        print(progression_outcome,"-",Main_List1[n][0],",",Main_List1[n][1],",",Main_List1[n][2])
        n+=1
        
    print()

### .............. End of the Part 2 ..............


### .............. Part 3 - Text File ..............

    # Create Text files for write Progression data
    Text_file=open("Progression data.txt","w")

    # Add to text file print statements
    Text_file.write("Part 3:\n")

    # Writing the data in the "Main_List1" and "Main_List2" lists to a text file
    n=0 ## Indexing variable
    for progression_outcome in Main_List2:
    
        # Add to text file print statements
        Text_file.write(progression_outcome)
        Text_file.write(" - ")
        Text_file.write(str(Main_List1[n][0]))
        Text_file.write(" , ")
        Text_file.write(str(Main_List1[n][1]))
        Text_file.write(" , ")
        Text_file.write(str(Main_List1[n][2]))
        Text_file.write("\n")

        n+=1

    # Closing text file
    Text_file.close()

    # Open Text file for read Progression data
    Text_file=open("Progression data.txt","r")

    # Display the read data
    print(Text_file.read())

### .............. End of the Part 3 ..............

