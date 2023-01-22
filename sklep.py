
import datetime

while True:
  print("Wybierz opcję \n1. => Lista wszystkich produktów \n2. => Zakupy \n3. => Zakończ program")
  x = input("Wybierz 1, 2 lub 3: ")
  if x in ["1", "2", "3"]:
    break
 

products = {
    "001": ("Masło Extra", 6.50),
    "002": ("Chleb wiejski", 4.50),
    "003": ("Makaron Babuni", 9.20),
    "004": ("Dżem truskawkowy", 8.10),
    "005": ("Kiełbasa myśliwska", 29.00),
    "006": ("Szynka konserwowa", 22.00),
    "007": ("Chipsy paprykowe", 6.00),
    "008": ("Serek wiejski", 3.50),
    "009": ("Sól kuchenna", 2.70),
    "010": ("Cukier kryształ", 3.20),
}


while x == "1":
    print("KOD KRESKOWY | NAZWA | CENA")
    for code, (name, price) in products.items():
        print(f"{code} | {name} | {price} zł")


    print("-------------")
    print("Wybierz opcję \n1. => Lista wszystkich produktów \n2. => Zakupy \n3. => Zakończ program")
    x = input("Wybierz 1, 2 lub 3: ")


if x == "3":
    exit()


purchased_products = {}

total_price = 0

VAT_RATE = 1.23
VAT_RATE1 = 0.23

done = False

while not done:
  product_code = input("Kod kreskowy lub wydruk paragonu(P): ")

  if product_code.upper() == "P":
    done = True
    continue

  if product_code in products:
      product_name, product_price = products[product_code]

      print(f"{product_name}")

      price = product_price
      rounded_price = round(price, 2)
      purchased_products[product_code] = (product_name, rounded_price)
      total_price += rounded_price
      total_price = round(total_price, 2)

      print(f"Cena łączna: {total_price:.2f} zł")

  else:
    print("Zły kod produktu. Spróbuj ponownie.")


total_price_with_vat = total_price / VAT_RATE
vat = round(total_price_with_vat, 2)


rest_vat = round(total_price - vat,2)

now = datetime.datetime.now()
purchase_date = now.strftime("%m/%d/%Y %H:%M:%S")

print("---------------------------------")
print("Paragon:")
print(f"Data zakupu: {purchase_date}")
print("---------------------------------")

for product_code, (product_name, product_price) in purchased_products.items():
  print(f"{product_name}: {product_price:.2f} zł")

print("---------------------------------")
print(f"Do zapłaty(brutto): {total_price}" " zł")
print(f"Do zapłaty(netto): {vat}" " zł")
print(f"Vat(23%) wynosi:{rest_vat}zł")
print("---------------------------------")
