import sys, random, csv

class magic8ball:
    def __init__(self,name):
        self.__name = name
        self.__mQuestions = []

    def __start_game(self):
        
        isTrue = True
        responses = ["IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT, YES","OUTLOOK LOOKS GOOD", "MOST LIKELY","IT IS DECIDELY SO", "WITHOUT A DOUBT","YES, DEFINETLY"]
        while isTrue:
            inp = input("Please ask a question!!\n")
            self.__mQuestions.append(inp)

            if inp == "":
                self.__write_questions()
                sys.exit()
            else:
                print(responses[random.randint(0,7)])

    def start_game(self):
        self.__start_game()

    def print_questions(self):
        print(self.__mQuestions)

    def __write_questions(self):
        MagicCsvFile = open("magic_questions.csv","a",newline='')
        writer = csv.writer(MagicCsvFile)
        writer.writerow(self.__mQuestions)
        MagicCsvFile.close()

magic = magic8ball("Jetty")
magic.start_game()
