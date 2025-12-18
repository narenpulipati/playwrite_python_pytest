
import pytest
from playwright.sync_api import Page, expect


def test_css_locator(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    products = page.locator("//a[contains(text(), 'computer')]")
    products_count = products.count()
    print("products count : ", products_count)
    expect(products).to_have_count(products_count)
#printing the product names individually
    '''print(products.first.text_content())
    print(products.last.text_content())
    print(products.nth(1).text_content())
    print(products.nth(0).text_content())'''
#using for loop to print the products list
    print("\n Below are the products list:\n")
    for product in range(products_count):
        print(products.nth(product).text_content())
#Below is the play-write inbuilt
    '''product_names=products.all_text_contents()
    for i in product_names:
        print(i)'''