import os
import pytest

from playwright.sync_api import sync_playwright

from main.bose import get_meta_data

@pytest.mark.parametrize(
    'expected,link',
    [
        (
                {
                    'title': 'QuietComfort® 35 headphones ear cushion kit',
                    'description': 'Replace lost or damaged earcup cushions for your QuietComfort 35 headphones. Sold '
                                   'as a pair. ',
                    'image': 'file://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/global/accessories'
                             '/headphones/qc35_acc_earcup/qc35_ear_cushion_kit_acc_black_EC_00.psd/_jcr_content'
                             '/renditions/cq5dam.web.320.320.png',
                    'is_currently_unavailable': False,
                    'price': 39.9
                },
                f'file://{os.path.dirname(__file__)}/files_for_testing/bose/qc35-part-1.html'
        ),
        (
                {
                    'title': 'Bose Sleepbuds™ II',
                    'description': 'Sleep better with Bose sleepbuds. Relaxing meditation helps you fall asleep, '
                                   'soothing sounds keeping you asleep, and a built-in alarm only you can hear.',
                    'image': 'file://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/global/products'
                             '/headphones/noise_masking_sleepbuds_ii/product_silo_images/SBII_PP_Ecom_Silo'
                             '-1_1200x1022_web.png/_jcr_content/renditions/cq5dam.web.320.320.png',
                    'is_currently_unavailable': False,
                    'price': 249.95
                },

                f'file://{os.path.dirname(__file__)}/files_for_testing/bose/noise-part-1.html'
        ),
    ]
)
def test_work_products(expected, link):

    with sync_playwright() as p:
        iphone_11 = p.devices['iPhone 11 Pro']
        browser = p.webkit.launch(headless=True)
        context = browser.new_context(**iphone_11)
        page = context.new_page()

        actual = get_meta_data(page, link)

        browser.close()

        assert expected.get('title') == actual.get('title')
        assert expected.get('description') == actual.get('description')
        assert expected.get('is_currently_unavailable') == actual.get('is_currently_unavailable')
        assert expected.get('price') == actual.get('price')
        assert expected.get('image') == actual.get('image')
