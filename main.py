import os
import time
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
        print("Esperando 1 hora para el próximo chequeo...")
        time.sleep(3600)

if __name__ == "__main__":
    main()