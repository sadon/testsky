# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Test7Auth(unittest.TestCase):

    print("Тестирование кнопок соц.сетей на Google Chrome в русском ЛК")
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.driver.implicitly_wait(30)


        self.driver.get("https://cab-test7.skyway.capital")
        self.assertIn("Sky Way", self.driver.title)
        print("Открыли форму авторизации сайта cab-test7.skyway.capital")

    def test_auth_in_test7(self):
        self.login__form_email = self.driver.find_element_by_name("LoginForm[email]")
        self.login__form_email.send_keys("n.chagdurova@skyway.capital")
        self.login__form_email.send_keys(Keys.RETURN)
        print("Ввели логин")
        self.login__form_password = self.driver.find_element_by_name("LoginForm[password]")
        # self.login__form_password.send_keys("Xfulehjd")
        # self.login__form_password.send_keys(Keys.RETURN)
        # self.mes = self.driver.find_element_by_xpath("/html/body/div/div/div/form/span")
        # self.assertIn("The username or password you entered is incorrect.", self.mes)
        # self.login__form_password.clear()
        self.login__form_password.send_keys("Xfulehjdf!1")
        self.login__form_password.send_keys(Keys.RETURN)
        print("Ввели пароль")
        self.assertIn("Sky Way", self.driver.title)
        print("Переход в ЛК")
        # self.cabinet = self.driver.find_element_by_link_text("Go to Partner Cabinet")
        # self.assertTrue("Go to Partner Cabinet", self.cabinet)
        # self.cabinet.click()
        # self.cabinet.implicitly_wait(5)
        time.sleep(3)

        print('Проверка  кнопки "go to Partner Cabinet":')
        self.cabinet = self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-warning']")
        self.cabinet.click()
        print('Кнопка "go to Partner Cabinet" работает')
        time.sleep(2)
        self.driver.execute_script("window.history.go(-1)")
        time.sleep(2)
        print('Возврат на главную страницу')
        print('Проверка пакета иннотранс:')
        self.innotrans = self.driver.find_element_by_xpath("//a[@class='innotrans-buy']")
        time.sleep(2)
        self.innotrans.click()
        time.sleep(2)
        print("Выбрали пакет INNOTRANS")
        self.innotrans_pay_in = self.driver.find_element_by_xpath("//input[@id='pay-w-acc']")
        time.sleep(2)
        self.innotrans_pay_in.click()
        time.sleep(2)
        print('Выбрали оплату с внутренних кошельков')
        self.innotrans_main = self.driver.find_element_by_xpath("//input[@id='input5']")
        time.sleep(2)
        self.innotrans_main.clear()
        self.innotrans_main.send_keys("1000")
        time.sleep(2)
        self.innotrans_main.send_keys(Keys.RETURN)
        time.sleep(2)
        print('Ввели необходимую сумму в размере 1000$')
        self.innotrans_checkout = self.driver.find_element_by_xpath("//input[@class='btn pay-btn do-pay-button col-xs-12']")
        time.sleep(2)
        self.innotrans_checkout.click()
        time.sleep(2)
        print('Далее нажимаем кнопку "Перейти"')
        self.innotrans_yes = self.driver.find_element_by_xpath("//button[@id='progressStart']")
        time.sleep(2)
        self.innotrans_yes.click()
        time.sleep(3)
        print('Во всплывающем окне подтверждаем инвестицию')
        self.innotrans_agree = self.driver.find_element_by_xpath("//input[@id='agree']")
        time.sleep(2)
        self.innotrans_agree.click()
        time.sleep(3)
        print('Принимаем условия договора')
        self.innotrans_invest = self.driver.find_element_by_xpath("//button[@id='buy-btn']")
        time.sleep(2)
        self.innotrans_invest.click()
        time.sleep(5)
        print('Нажимаем "Инвестировать"')
        self.assertIn('Мои сертификаты', self.driver.title)
        print('После покупки иннотранса перещли в раздел "Мои сертификаты"')
        print('Тест окончен успешно!')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
