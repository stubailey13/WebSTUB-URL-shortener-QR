import string
import secrets
from tinydb import TinyDB
from tinydb import Query
import qrcode
Web = Query()
db = TinyDB("urls.json")


# User Options
def user_options():
    print("1. GENERATE website QR")
    print("2. SHORTEN a website")
    print("3. SEARCH a webSTUB")
    return


# Generate website QR
def generate_qr():
    x = input("Website to generate QR: ")
    qr = qrcode.QRCode(version=1,
                       box_size=10,
                       border=4)
    qr.add_data(x)
    qr.make(fit=True)
    img = qr.make_image(fill_color='blue',
                        back_color='white')
    img.save("WebSTUB.png")
    print("Your WebSTUB has successfully been created!")
    return


# Shorten & Save URLs
def url_stub():
    long_url = input("Input URL: ")
    alphabet = string.ascii_letters + string.digits
    short_url = ''.join(secrets.choice(alphabet) for i in range(7))
    db.insert({'long_url': long_url, 'short_url': short_url})
    print("Short URL STUB successfully created: " + short_url)
    return


# Search URL STUB
def search_url():
    user_search = input("Paste short URL STUB: ")
    result = db.get(Web.short_url == user_search)
    print(result.get('long_url'))
    return

