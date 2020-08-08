from rivescript import RiveScript
swecha=rivescript.RiveScript()
swecha.load_file('responses.rive')
swecha.sort_replies() 

while(1):
        question=input("Enter the Question:>")
        print(swecha.reply("localuser",question))
