from fastapi import FastAPI, responses, Body
import json
import requests
from fastapi.responses import JSONResponse
import os

app = FastAPI()

latest_gsi_data = {}
prev_k = 0
prev_d = 0
@app.post('/')
def do_post_cs2(data = Body()):
    try:
        if data:
                global latest_gsi_data
                latest_gsi_data = data
                print(f"Получены данные GSI")
                l = latest_gsi_data["player"]
                s = l["match_stats"]
                current_k = s["kills"]
                current_d = s["deaths"]
                global prev_k
                global prev_d
                if prev_k != current_k:
                     os.system('cd "C:\Program Files (x86)\Steam\steamapps\common\Soundpad" & Soundpad -rc DoPlaySoundFromCategory(-1,2)')
                     prev_k = current_k
                else:
                     pass
                if prev_d != current_d:
                     os.system('cd "C:\Program Files (x86)\Steam\steamapps\common\Soundpad" & Soundpad -rc DoPlaySoundFromCategory(-1,1)')
                     prev_d = current_d
                else:
                     pass
    except Exception as e:
         print(f"Ошибка обработки POST: {e}")

@app.get('/gsi')
def do_get_cs2():
     if latest_gsi_data:
          return JSONResponse(content=latest_gsi_data)
     else:
          return {"error": "No data yet"}
     