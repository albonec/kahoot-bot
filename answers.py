import urllib.request as ur
import json as j

url = "https://play.kahoot.it/rest/kahoots/" + input("GAME ID: ")

colours = ["red", "blue", "yellow", "green"]
json = j.loads(ur.urlopen(url).read())["questions"]


for index, slide in enumerate(json):
    for i in range(len(slide.get("choices"))):
        
        if slide["choices"][i]["correct"]:
            
            if len(slide.get("choices")) == 2:
                coulours_list = coulours[:2][::-1]
                
            else:
                coulours_list = colours
            
            print(f"{index+1}:\n{slide['choices'][i].get('answer')}\n{colours_list[i]}\n")
