def get_meta_data(page, url: str) -> dict:
    page.goto(url)

    price = -1
    is_currently_unavailable = "Currently unavailable" in page.query_selector(".a-color-price").inner_text()

    if not is_currently_unavailable:
        price = page.evaluate(
            """
            () => {
             const rawText = document.querySelector("span[dir='ltr']").innerText.replace(/\$\s/g, "").trim() // "13 99"
             const formatedText = rawText.split(" ").join(".") // "13.99"

             return parseFloat(formatedText)
             }
            """
        )

    output = {
        "title": page.evaluate('() => document.querySelector("#title").textContent.trim()'),
        "description": page.query_selector('//*[contains(@id,"productDescription")]').inner_text(),
        "is_currently_unavailable": is_currently_unavailable,
        'price': price,
        "image": page.evaluate('()=> document.querySelector("img#main-image").src')
    }

    return output
