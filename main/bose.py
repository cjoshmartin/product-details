import time

def matcher(url):
    return "bose.com" in url


def get_meta_data(page, url: str) -> dict:
    page.goto(url)
    title = page.query_selector(".bose-title").inner_text()
    description = page.evaluate("""()=> {
         const description = document.querySelector("meta[name='description'")
         return description.attributes["content"].value
    }""")

    page.click('a[title="BUY NOW"]')

    time.sleep(6)
    image = page.evaluate("() => document.querySelector('.bose-cartItem__image img').src")
    price = page.query_selector(".bose-shoppingBag__paymentTotalRowPrice").inner_text()

    return {
        'title': title,
        'description': description,
        'image': image,
        'is_currently_unavailable': False,
        'price': float(price[1:]),
    }
