def temp():
    '''''
        retorna a temperatura, a probabilidade de chuva e a umidade
    '''''
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options

    try:
        option = Options()
        option.headless = True
        browser = Firefox(options=option)
        browser.save_screenshot('screen.png')
        browser.get('https://www.google.com/search?client=firefox-b-d&q=cilma+em+curitiba')
        temp = browser.find_element_by_id('wob_tm').text
        prob_chuv = browser.find_element_by_id('wob_pp').text
        umi = browser.find_element_by_id('wob_hm').text

        browser.close()
        return temp, prob_chuv, umi
    except:
        print('talvez sua internet não esteja ligada')


print(temp())