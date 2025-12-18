from playwright.sync_api import Page,expect

# below function is related to checking the date picker
def test_picker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")
    date_input.click()
    # check the datepicker visible or not
    page.locator('.ui-datepicker').is_visible()
    # page.locator("span:has-text('Prev')").click()
    # page.get_by_title('Prev').click()  #click on previous month button
    page.get_by_title('Next').click()  # click on next month button

    page.locator("a[data-date='13']").click()  # selecting the date
    date_input = page.locator("#datepicker")  # navigating to selected date picket input box

    selected_date = date_input.input_value()  # input_value() is to get the dynamic values text
    print("Selected date:", selected_date)

#below function is related to static date picker

def test_date_picker(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #click on date picker input
    date_input=page.locator("#datepicker")
    date_input.click()


    target_month = "January"
    target_year = "2025"
    target_day = "25"


    # Loop with safety limit (max 20 years = 240 months)
    for _ in range(240):
        # Read displayed month and year
        displayed_month = page.locator(".ui-datepicker-month").text_content()
        displayed_year = page.locator(".ui-datepicker-year").text_content()

        # Check if target month and year reached
        if displayed_month == target_month and displayed_year == target_year:
            break

        # Navigate backward (for past dates)
        page.locator("span:has-text('Prev')").click()



    # Click the day (a[data-date='25'])
    page.locator(f"a[data-date='{target_day}']").click()

    # Get value from the INPUT box, not the <a>
    selected_date = date_input.input_value()
    print("Selected date:", selected_date)
#below function is related to drop down date picker
def test_date_picker1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

#input date
    target_day = "11"
    target_month_index = "5"   # June = index 5 (0-based)
    target_year = "2024"
#locating the calendar
    date_input = page.locator("input[name='SelectedDate']")
    date_input.click()
    expect(date_input).to_be_visible()

#locating month/year dropdowns to appear
    month_dropdown = page.locator(".ui-datepicker-month")
    year_dropdown = page.locator(".ui-datepicker-year")

#validating month/year dropdowns are visible
    expect(month_dropdown).to_be_visible()
    expect(year_dropdown).to_be_visible()

#Select year & month using select_option method
    year_dropdown.select_option(target_year)
    month_dropdown.select_option(value=target_month_index)

#Select day
    page.locator(f"a[data-date='{target_day}']").click()
    selected_date = page.locator("input[name='SelectedDate']").input_value()
    print("Selected Date: ", selected_date)
