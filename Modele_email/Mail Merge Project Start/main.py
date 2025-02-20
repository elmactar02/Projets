#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



file_model = open("Input/Letters/starting_letter.txt","r")
file_name = open("Input/Names/invited_names.txt","r")

model_txt = file_model.read()
list_name = file_name.readlines()

for name in list_name:
    name = name.replace("\n",'')
    new_file_name = "Output/ReadyToSend/letter_" + name + ".txt"
    new_file = open(new_file_name,"w")
    new_file.write(model_txt.replace("[name]",name))