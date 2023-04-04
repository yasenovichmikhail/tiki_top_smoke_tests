from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = "https://tikitop.io/"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_login_email_success(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    signup_button = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    signup_button_text_act = signup_button.text
    signup_button_text_exp = "Sign Up"
    assert signup_button_text_act == signup_button_text_exp, f"expected {signup_button_text_exp}, got {signup_button_text_act}"
    signup_button.click()
    login_tab = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")))
    login_tab.click()
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("alisson.ginter@gmail.com")
    input_password = browser.find_element(By.NAME, "password")
    input_password.send_keys("qwertyasd")
    login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")))
    login_button.click()
    auth_text = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")
    auth_text_act = auth_text.text
    auth_text_exp = "Profile"
    assert auth_text_act == auth_text_exp, f"expected {auth_text_exp}, got {auth_text_act}"


def test_login_facebook_success(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    signup_button = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    signup_button_text_act = signup_button.text
    signup_button_text_exp = "Sign Up"
    assert signup_button_text_act == signup_button_text_exp, \
        f"expected {signup_button_text_exp}, got {signup_button_text_act}"
    signup_button.click()
    login_tab = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")))
    login_tab.click()
    facebook_button = browser.find_element(
        By.XPATH,
        "//button[@class='AuthorizationServices_btnLogin__txbzD AuthorizationServices_iconFacebook__0Fg5_']")
    facebook_button.click()
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    facebook_input_email = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='email']")))
    facebook_input_email.send_keys("yasenovich.mikhail@mail.ru")
    facebook_input_pass = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@id='pass']")))
    facebook_input_pass.send_keys("mnrvP888")
    facebook_login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//label[@id='loginbutton']")))
    facebook_login_button.click()
    browser.switch_to.window(first_window)
    profile_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")))
    profile_button.click()
    my_profile_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@class='ModalButtonProfile_item__FhMKh'][1]")))
    my_profile_button.click()
    facebook_profile_text = browser.find_element(By.XPATH, "//p[@class='UserProfile_email_header__70AZB']")
    facebook_profile_text_exp = "Logged in with Facebook"
    facebook_profile_text_act = facebook_profile_text.text
    assert facebook_profile_text_act == facebook_profile_text_exp, \
        f"expected {facebook_profile_text_exp}, got {facebook_profile_text_act}"


def test_open_profile(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    signup_button = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    signup_button_text_act = signup_button.text
    signup_button_text_exp = "Sign Up"
    assert signup_button_text_act == signup_button_text_exp, f"expected {signup_button_text_exp}, got {signup_button_text_act}"
    signup_button.click()
    login_tab = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")))
    login_tab.click()
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("bobbyngayer@gmail.com")
    input_password = browser.find_element(By.NAME, "password")
    input_password.send_keys("qwertyasd")
    login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")))
    login_button.click()
    profile_button = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK ButtonHeaderProfile_button__756EG']")
    profile_button.click()
    my_profile_button = browser.find_element(By.XPATH, "//li[@class='ModalButtonProfile_item__FhMKh'][1]")
    my_profile_button.click()
    your_profile_text = browser.find_element(By.XPATH, "//h2[@class='AccountComponent_title__gZO_n']")
    your_profile_text_exp = "YOUR PROFILE"
    your_profile_text_act = your_profile_text.text
    assert your_profile_text_act == your_profile_text_exp, f"expected {your_profile_text_exp}, got {your_profile_text_act}"


def test_main_landing(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    tiki_top_logo = browser.find_element(By.XPATH, "//img[@alt='Tiki Top']")
    tiki_top_logo.click()
    home_page = browser.find_element(
        By.XPATH, "//h1[@class='HeaderOffer_title__XSSqh']")
    home_page_text_exp = "BOOST YOUR TIKTOK PROFILE & VIDEOS"
    home_page_text_act = home_page.text
    assert home_page_text_act == home_page_text_exp, f"expected {home_page_text_exp}, got {home_page_text_act}"
    boost_your_tiktok = browser.find_element(
        By.XPATH, "//section[@class='container HeaderOffer_headerOffer__0Nk4c']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", boost_your_tiktok)
    get_more_info1_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed2__33NJf']")
    get_more_info1_button.click()
    make_your_order_text = browser.find_element(
        By.XPATH, "//h2[@class='MakeOrder_title__t4vgt']")
    make_your_order_text_exp = "MAKE YOUR ORDER"
    make_your_order_text_act = make_your_order_text.text
    assert make_your_order_text_exp == make_your_order_text_act, f"expected {make_your_order_text_exp}, got {make_your_order_text_act}"
    browser.back()
    what_we_offer = browser.find_element(
        By.XPATH, "//section[@class='container'][1]")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", what_we_offer)
    get_more_info2_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorRed__y2rlJ LinkButton_sizeBig__7aVP_']")
    get_more_info2_button.click()
    assert make_your_order_text_exp == make_your_order_text_act, f"expected {make_your_order_text_exp}, got {make_your_order_text_act}"
    browser.back()
    what_done = browser.find_element(
        By.XPATH, "//section[@class='container DoneOrders_container__aI7tA']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", what_done)
    promotion_formats = browser.find_element(
        By.XPATH, "//section[@class='container'][2]")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", promotion_formats)
    get_more_info3_button = browser.find_element(
        By.XPATH,
        "//div[@class='PromotionFormatItem_container__f_OBE PromotionFormatItem_containerGetMore__HuFNd']//a[@class='LinkButton_link___jzSK LinkButton_colorWhite__A_Qx3']")
    get_more_info3_button.click()
    assert make_your_order_text_exp == make_your_order_text_act, f"expected {make_your_order_text_exp}, got {make_your_order_text_act}"
    browser.back()
    any_questions = browser.find_element(
        By.XPATH, "//section[@class='container AnyQuestions_container__7229q']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", any_questions)
    get_more_info4_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorBlack__WwvPN']")
    get_more_info4_button.click()
    faq_text = browser.find_element(
        By.XPATH, "//h1[@class='FaqInfo_title__qU5w9']")
    faq_text_exp = "POPULAR QUESTIONS"
    faq_text_act = faq_text.text
    assert faq_text_act == faq_text_exp, f"expected {faq_text_exp}, got {faq_text_act}"
    browser.back()
    contact_us_main_button = browser.find_element(
        By.XPATH, "//a[@class='LinkButton_link___jzSK LinkButton_colorWhiteWithBorder__zLVqH']")
    contact_us_main_button.click()
    contact_us_text = browser.find_element(
        By.XPATH, "//h1[@class='ContactUsForm_title__F_181']")
    contact_us_text_exp = "GET IN TOUCH"
    contact_us_text_act = contact_us_text.text
    assert contact_us_text_exp == contact_us_text_act, f"expected {contact_us_text_exp}, got {contact_us_text_act}"


def test_faq(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    faq_tab = browser.find_element(By.LINK_TEXT, "FAQ")
    faq_tab.click()
    question1_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][1]")
    question1_open.click()
    question1_text_exp = "Is it safe to promote from you?"
    question1_text_act = question1_open.text
    assert question1_text_exp == question1_text_act, \
        f"expected {question1_text_exp}, got {question1_text_act}"
    question1_close = browser.find_element(
        By.XPATH, "//summary[@class='FaqInfoItem_faqSummary__eKNYE'][1]")
    question1_close.click()
    question2_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][2]")
    question2_open.click()
    question2_text_exp = "What are the promotion limits?"
    question2_text_act = question2_open.text
    assert question2_text_exp == question2_text_act, \
        f"expected {question2_text_exp}, got {question2_text_act}"
    question2_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][2]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question2_close.click()
    question3_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][3]")
    question3_open.click()
    question3_text_exp = "What are the accepted payment methods?"
    question3_text_act = question3_open.text
    assert question3_text_exp == question3_text_act, \
        f"expected {question3_text_exp}, got {question3_text_act}"
    question3_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][3]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question3_close.click()
    question4_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][4]")
    question4_open.click()
    question4_text_exp = "Can I promote someone else's account?"
    question4_text_act = question4_open.text
    assert question4_text_exp == question4_text_act, \
        f"expected {question4_text_exp}, got {question4_text_act}"
    question4_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][4]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question4_close.click()
    question5_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][5]")
    question5_open.click()
    question5_text_exp = "What is Order?"
    question5_text_act = question5_open.text
    assert question5_text_exp == question5_text_act, \
        f"expected {question5_text_exp}, got {question5_text_act}"
    question5_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][5]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question5_close.click()
    question6_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][6]")
    question6_open.click()
    question6_text_exp = "What number of days is better to choose for an order?"
    question6_text_act = question6_open.text
    assert question6_text_exp == question6_text_act, \
        f"expected {question6_text_exp}, got {question6_text_act}"
    question6_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][6]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question6_close.click()
    question7_open = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][7]")
    question7_open.click()
    question7_text_exp = "How to stop an active order?"
    question7_text_act = question7_open.text
    assert question7_text_exp == question7_text_act, \
        f"expected {question7_text_exp}, got {question7_text_act}"
    question7_close = browser.find_element(
        By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][7]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    question7_close.click()
    # question8_open = browser.find_element(
    #     By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][8]")
    # question8_open.click()
    # question8_text_exp = "Can I do multiple orders on 1 post?"
    # question8_text_act = question8_open.text
    # assert question8_text_exp == question8_text_act, \
    #     f"expected {question8_text_exp}, got {question8_text_act}"
    #
    # question8_close = browser.find_element(
    #     By.XPATH, "//li[@class='FaqInfoItem_item__awC4B'][8]//summary[@class='FaqInfoItem_faqSummary__eKNYE']")
    # question8_close.click()


def test_contact_us(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    contact_us_tab = browser.find_elements(By.LINK_TEXT, "Contact Us")[1]
    contact_us_tab.click()
    contact_us_text = browser.find_element(
        By.XPATH, "//h1[@class='ContactUsForm_title__F_181']")
    contact_us_text_exp = "GET IN TOUCH"
    contact_us_text_act = contact_us_text.text
    assert contact_us_text_exp == contact_us_text_act, f"expected {contact_us_text_exp}, got {contact_us_text_act}"
    first_name = browser.find_element(By.ID, 'name')
    first_name.send_keys("TEST")
    email = browser.find_element(By.ID, 'email')
    email.send_keys("TEST@fexbox.org")
    message = browser.find_element(By.ID, 'message')
    message.send_keys("TEST TEST TEST TEST TEST TEST TEST")
    send_message_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='CustomButton_btn__22u2s CustomButton_colorRed__g7yY3']")))
    send_message_button.click()
    sent_message_popup = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//h4[@class='ModalSuccess_title__EMOMJ']")))
    sent_message_text_exp = 'Your message has been sended'
    sent_message_text_act = sent_message_popup.text
    assert sent_message_text_exp == sent_message_text_act, \
        f"expected {sent_message_text_exp}, got {sent_message_text_act}"
    okay_button = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeModalAsk__sQjdZ']"
    )
    okay_button.click()
    assert contact_us_text_exp == contact_us_text_act, f"expected {contact_us_text_exp}, got {contact_us_text_act}"


def test_login_incorrect_password(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    signup_button = browser.find_element(
        By.XPATH,
        "//button[@class='CustomButton_btn__22u2s CustomButton_colorWhite__MeJq0 CustomButton_btnSignUp__1ijqK']")
    signup_button_text_act = signup_button.text
    signup_button_text_exp = "Sign Up"
    def signup(signup_button_text_act, signup_button_text_exp):
        assert signup_button_text_act == signup_button_text_exp, f"expected {signup_button_text_exp}, got {signup_button_text_act}"
    signup(signup_button_text_act, signup_button_text_exp)
    signup_button.click()
    login_tab = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='AuthorizationTypeItem_item__2IwVY'][2]")))
    login_tab.click()
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("bobbyngayer@gmail.com")
    input_password = browser.find_element(By.NAME, "password")
    input_password.send_keys("qwertyasdasd")
    login_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             "//button[@class='CustomButton_btn__22u2s CustomButton_colorAqua__TKZR6 CustomButton_typeAuth__m__ns']")))
    login_button.click()
    incorrect_data_text = browser.find_element(
        By.XPATH, "//span[@class='ModalBase_errors__rYDQx']")
    incorrect_data_text_act = incorrect_data_text.text
    incorrect_data_text_exp = "No correct data..."
    assert incorrect_data_text_exp == incorrect_data_text_act, f"expected {incorrect_data_text_exp}, got {incorrect_data_text_act}"