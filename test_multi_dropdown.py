from playwright.sync_api import Page,expect

def test_multi_dropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    dropdown=page.locator("#colors>option")

    print("Number of elements available on dropdown is :", dropdown.count())
    expect(dropdown).to_have_count(7)

    dropdown.nth(index=3).click()# using index


    red_option=page.locator("#colors").select_option("Red") #using value
    page.locator("#colors").select_option(label="Blue")  # using lable
    page.locator("#colors").select_option(["Yellow", "Blue"])


    #options=page.locator("#colors>option").all_text_contents()  # unsorted dropdown
    options = page.locator("#animals>option").all_text_contents() # sorted dropdown
    for text in options:
        print(text.strip())
    sorted_options=sorted(options)
    if sorted_options==options:
        print("List is sorted: ")
    else:
        print("List is not sorted: ")




