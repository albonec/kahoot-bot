import urllib.request as ur
import json as j

def get_answers(id):  
    url = "https://play.kahoot.it/rest/kahoots/"+id

    color_list = ["red", "blue", "yellow", "green"]
    json = j.loads(ur.urlopen(url).read())["questions"]

    for index, slide in enumerate(json):
        for i in range(len(slide.get("choices"))):
            if slide["choices"][i]["correct"]:
                print(f"{index+1}:\n{slide['choices'][i].get('answer')}\n{color_list[i]}\n")
        
while True:
        get_answers(input("[-] QUIZ ID: "))
       
