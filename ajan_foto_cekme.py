import requests
import os

# API URL'si
API_URL = "https://valorant-api.com/v1/agents"

# Kayıt klasörünü oluştur
SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)

# API'den veri çek
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()["data"]  # API sonucu JSON formatında
    for agent in data:
        if agent["displayIconSmall"]:  # İkon varsa
            agent_name = agent["displayName"].lower().replace(" ", "_")  # Dosya ismi için
            if agent_name == "kay/o":
                agent_name = "kayo"
            img_url = agent["displayIconSmall"]
            img_path = os.path.join(SAVE_DIR, f"{agent_name}.png")

            # İkonu indir
            img_data = requests.get(img_url).content
            with open(img_path, "wb") as img_file:
                img_file.write(img_data)

            print(f"{agent_name}.png kaydedildi.")
else:
    print("API'ye bağlanılamadı. Hata kodu:", response.status_code)
