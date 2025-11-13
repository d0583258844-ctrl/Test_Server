from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get("/test")
def basic_print():
    return {"msg": "Hello from test"}

@app.get("/test/{nam}")
def get_name_and_save(name: str):
    file = "names.txt"
    with open(file, "a") as f:
       f.write(name+"\n")
    return {"msg": "saved user"}


@app.post("/caesar")
def caesar_encrypted_decrypted(item:dict):
    text = item["text"]
    text1 = text.replace(" ","")
    alph_list =[
                'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z'
            ]
    new_word = ""
    if item["mode"] == "encrypt":
        for ch in text1:
            ch1 = alph_list.index(ch)
            new_word += alph_list[(ch1 + item["offset"]) % 26] 
        return  {"encrypted_text": new_word } 

    elif item["mode"] == "decrypt":
        for ch in text1:
            ch1 = alph_list.index(ch)
            new_word += alph_list[(ch1 - item["offset"]) % 26] 
    return  {"decrypted_text": new_word}

