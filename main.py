import urllib.request as ur
import json as j
from threading import Thread
from kahoot import client


def get_answers(id):  
    url = f"https://play.kahoot.it/rest/kahoots/{id}"

    color_list = ["red", "blue", "yellow", "green"]
    json = j.loads(ur.urlopen(url).read())["questions"]

    for index, slide in enumerate(json):
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"]:
                if len(slide.get("choices")) == 2:
                    color = color_list[:2][::-1]
                else:
                    color = color_list

                print(f"{index+1}:\n{slide['choices'][i].get('answer')}\n{color_list[i]}\n")
        
        
def join_game(id, name):
    bot = client()
    bot.join(id, name)

    
def main():
    option = int(input("\n[1] ANSWERS\n[2] FLOODER\n"))
    
    if option == 1:
        quiz_id = input("[-] QUIZ ID: ")
        get_answers(quiz_id)
        
    elif option == 2:
        bot_count = int(input("[-] NUMBER OF BOTS: "))
        game_id = int(input("[-] GAME PIN: "))
        for i in range(bot_count): 
            Thread(target=join_game(game_id, str(i))).start()

    else:
        print("Invalid Option")
        main()
    

if __name__=="__main__":
    main()
