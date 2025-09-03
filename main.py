import os
import time
import random
from dotenv import load_dotenv
from utils.price_checker import check_price

load_dotenv()

URL = os.environ["URL"]
BUY_PRICE = 6000

def main():
    while True:
        try:
            check_price(URL, BUY_PRICE)
        except Exception as e:
            print(f"Error: {e}")
        #Generate a random sleep time betwen 
        sleep_time = random.randint(3600, 10800)
        print(f"Esperando {sleep_time // 3600} horas y {(sleep_time % 3600) // 60} minutos para el próximo chequeo...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()