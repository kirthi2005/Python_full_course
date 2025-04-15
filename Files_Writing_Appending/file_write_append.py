# file append
# welcome_message = open("hello.txt","a")
# welcome_message.write("Let's chat")
# welcome_message.write("\nHello,how are you?")

#write into file. w - overwrite the file
# welcome_message = open("hello.txt","w")
# welcome_message.write("\nHello,how are you?")

# write mode- if file doesn't exist it will create one
# welcome_message = open("hello.txt1","w")
# welcome_message.write("Welcome everyone!")

welcome_message = open("index.html","w")
welcome_message.write("<p>Vivek</p>")

welcome_message.close()

