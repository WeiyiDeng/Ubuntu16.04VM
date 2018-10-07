from splinter import Browser

browser = Browser()
browser.visit('https://holland2stay.com/residences.html?available_to_book=179&p=2')
# browser.fill('q', 'splinter - python acceptance testing for web applications')
# browser.find_by_name('btnK').click()

if browser.is_text_present('1,050.00'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

# browser.quit()

find_h=browser.find_by_css('div[class="price"]')
for i in find_h:
    print(i.text)
