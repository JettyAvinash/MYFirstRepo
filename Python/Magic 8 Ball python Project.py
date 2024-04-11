import sys,random

# Method - 1
# responses = { 
#     1 : "IT IS CERTAIN",
#     2 : "YOU MAY RELY ON IT",
#     3 : "AS I SEE IT, YES",
#     4 : "OUTLOOK LOOKS GOOD",
#     5 : "MOST LIKELY",
#     6 : "IT IS DECIDELY SO",
#     7 : "WITHOUT A DOUBT",
#     8 : "YES, DEFINETLY"
# }

# inp = input("Ask the Magic 8 Ball a question?")
# val = random.randint(1,8)
# for val in responses.keys():
#     if len(inp)>0:    
#         print(responses.get(val))
#         inp = input("Ask the Magic 8 Ball a question?")
#         val = random.randint(1,8)
#         continue
#     else:
#         sys.exit()

# Method - 2

responses = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT, YES","OUTLOOK LOOKS GOOD", "MOST LIKELY","IT IS DECIDELY SO", "WITHOUT A DOUBT","YES, DEFINETLY"]
istrue = True

while istrue:
    inp = input("Please ask a question")
    if inp == "":
        sys.exit()
    else:
        print(responses[random.randint(0,7)])
