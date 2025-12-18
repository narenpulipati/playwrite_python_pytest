from os import waitpid

from playwright.sync_api import Page, expect


def test_intro(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_title("Automation Testing Practice")
    expect(page).to_have_title("Automation Testing Practice")
    page.locator('id=monday').check()
    page.wait_for_timeout(2000)
    page.get_by_text('Online Trainings').click()

    page.wait_for_timeout(2000)
    page.get_by_title('SDET-QA')


    page.close()