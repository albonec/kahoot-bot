import urllib.request as ur
import json as j
from threading import Thread
from kahoot import client


def answers(id):  
    # Get Kahoot Quiz Answers
    url = "https://play.kahoot.it/rest/kahoots/"+id

    colors = ["red", "blue", "yellow", "green"]
    json = j.loads(ur.urlopen(url).read())["questions"]

    for index, slide in enumerate(json):
        for i in range(len(slide.get("choices"))):
            
            if slide["choices"][i]["correct"]:
                colors_list = colors[:2][::-1] if len(slide.get("choices")) == 2 else colors

                print(f"{index+1}:\n{slide['choices'][i].get('answer')}\n{colours_list[i]}\n")
        
        
def create_bot(id, name):
    # Join Kahoot Lobby w/ Bot
    bot = client()
    bot.join(id, name)

    
def main():
    option = int(input("\n[1] ANSWERS\n[2] FLOODER\n"))

    if option == 1:
        bot_count = int(input("[-] NUMBER OF BOTS: "))
        game_id = int(input("[-] GAME PIN: "))
        for i in range(bot_count): 
            Thread(target=create_bot(game_id, str(i))).start()

    elif option == 2:
        quiz_id = input("[-] QUIZ ID: ")
        answers(quiz_id)

    else: main()
    

if __name__=="__main__":
    main()
