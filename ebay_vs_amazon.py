from selenium import webdriver

input1 = input("what to search?")
browser = webdriver.Chrome("C:\\Users\Ariel\Downloads\chromedriver_win32\chromedriver")
browser.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="+ input1 +"&_sacat=0")
browser2 = webdriver.Chrome("C:\\Users\Ariel\Downloads\chromedriver_win32\chromedriver")
browser2.get("https://www.amazon.com/s?k=" + input1 + "&ref=nb_sb_noss_2")
print(len(browser2.find_elements_by_class_name("price-current")))

def print_ebay_resolt(brwsr, times):
    output1 = browser.find_elements_by_class_name("s-item__price")[times].get_attribute("innerHTML")
    output1 = output1.replace('<span class="DEFAULT"> to </span>'," to ")
    return "\t" + output1

def print_amazon_resolt(brwsr, times):
    output2 = browser2.find_elements_by_class_name("a-offscreen")[times].get_attribute("innerHTML")
    return "\t" + output2

print("the ebay results are:")
for i in range(20):
    print(print_ebay_resolt(browser, i))

print("the amazon results are:")
for j in range(20):
    print(print_amazon_resolt(browser2, j))

