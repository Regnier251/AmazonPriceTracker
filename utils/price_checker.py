import requests
from bs4 import BeautifulSoup
import smtplib
import os

def send_email(subject, body):
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:{subject}\n\n{body}".encode("utf-8")
        )

def check_price(url, buy_price):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    price_tag = soup.select_one("#corePrice_feature_div span.a-offscreen")

    if not price_tag:
        raise Exception("No se encontró el precio usando el selector alternativo.")

    price_text = price_tag.get_text().strip()
    price_as_float = float(price_text.replace("$", "").replace(",", ""))

    title_tag = soup.find(id="productTitle")
    title = title_tag.get_text().strip() if title_tag else "Sin título"

    print("Artículo:\n" + title)
    print(f"Precio: ${price_as_float:.2f}")

    if price_as_float < buy_price:
        message = f"{title} está en oferta por ${price_as_float:.2f}!"
        send_email("Alerta de precio en Amazon", message)
        print("Correo enviado.")
    else:
        print(f"Precio actual (${price_as_float:.2f}) es mayor que el límite (${buy_price}). No se envió correo.")
