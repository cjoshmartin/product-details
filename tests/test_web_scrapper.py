import os

from playwright.sync_api import sync_playwright

from main import get_meta_data


def test_work_on_book_link():
    expected = {
        'title': 'Living with Pattern: Color, Texture, and Print at Home (CLARKSON POTTER)',
        'description': 'Description\nProduct Description\nA design book filled with beautiful photography and clear ideas for how to use pattern to decorate your home.\xa0If you focus on pattern, from texture and color to furniture and textiles, everything else will fall into place. \n\xa0 \nPattern is the strongest element in any room. In Living with Pattern, Rebecca Atwood demystifies how to use that element, a design concept that often confounds and confuses, demonstrating how to seamlessly mix and layer prints throughout a house. She covers pattern usage you probably already have, such as on your duvet cover or in the living room rug, and she also reveals the unexpected places you might not have thought to add it: bathroom tiles, an arrangement of book spines in a reading nook, or windowpane gridding in your entryway. This stunning book showcases distinct uses of pattern in homes all over the country to inspire you to realize that an injection of pattern can enliven any space, helping to make it uniquely yours.\nAbout the Author\nRebecca Atwood received her BFA in painting from Rhode Island School of Design before beginning her career designing and consulting for major retailers. Today, she is a textile designer and an artist who blends traditional techniques with hand painting. Her interest in pattern is deeply rooted in her childhood on Cape Cod and her everyday observations of life in Brooklyn, where she lives with her husband.\n',
        'is_currently_unavailable': False,
        'price': 18.99,
        'image': 'https://images-na.ssl-images-amazon.com/images/I/61n7-mARLML._AC_SY400_.jpg'
    }

    link = f'file://{os.path.dirname(__file__)}/files_for_testing/living_with_pattern.html'

    with sync_playwright() as p:
        iphone_11 = p.devices['iPhone 11 Pro']
        browser = p.webkit.launch()
        context = browser.new_context(**iphone_11)
        page = context.new_page()

        actual = get_meta_data(page, link)

        browser.close()

        assert expected.get('title') == actual.get('title')
        assert expected.get('description') == actual.get('description')
        assert expected.get('is_currently_unavailable') == actual.get('is_currently_unavailable')
        assert expected.get('price') == actual.get('price')
        assert expected.get('image') == actual.get('image')


def test_works_on_item_link():
    expected = {
        'title': 'Learn to Solder Kit: Jitterbug',
        'description': 'Description\nLearn to Solder Kit: Jitterbug\n',
        'is_currently_unavailable': False,
        'price': 13.99,
        'image': 'https://images-na.ssl-images-amazon.com/images/I/41O2ZK4bq4L._AC_SY1000_.jpg'
    }
    link = f'file://{os.path.dirname(__file__)}/files_for_testing/learn_to_solder_bug.html'

    with sync_playwright() as p:
        iphone_11 = p.devices['iPhone 11 Pro']
        browser = p.webkit.launch()
        context = browser.new_context(**iphone_11)
        page = context.new_page()

        actual = get_meta_data(page, link)

        browser.close()

        assert expected.get('title') == actual.get('title')
        assert expected.get('description') == actual.get('description')
        assert expected.get('is_currently_unavailable') == actual.get('is_currently_unavailable')
        assert expected.get('price') == actual.get('price')
        assert expected.get('image') == actual.get('image')


def test_works_on_unavailable():
    expected = {
        'is_currently_unavailable': True,
        'price': -1,
    }
    link = f'file://{os.path.dirname(__file__)}/files_for_testing/unavailable_item.html'

    with sync_playwright() as p:
        iphone_11 = p.devices['iPhone 11 Pro']
        browser = p.webkit.launch()
        context = browser.new_context(**iphone_11)
        page = context.new_page()

        actual = get_meta_data(page, link)

        browser.close()

        assert expected.get('is_currently_unavailable') == actual.get('is_currently_unavailable')
        assert expected.get('price') == actual.get('price')
