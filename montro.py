import requests

from uuid import uuid4

headers = {
        "Content-Type": "application/json"
}

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
promo_url = 'https://discord.com/billing/partner-promotions/1180231712274387115/{}'

def generate():
    print("[*] Montro Alpha - Free Discord Nitro.")
    count = 0
    while True:
        try:
            request = requests.post(url, headers=headers, json={'partnerUserId':str(uuid4())})
            token = request.json().get('token')
            
            count += 1

            print("[Generated %s]" % count)
            print("\t\\__[%s]" % token[-10:])

            with open("nitro.txt", "a") as file:
                file.write(promo_url.format(token) + "\n")
        except Exception as error:
            print("error: %s" % error)

generate()
