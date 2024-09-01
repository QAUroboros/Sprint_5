from typing import Tuple

from selenium.webdriver.common.by import By


LOGIN_PAGE_LINK = (By.XPATH, "//a[contains(@href, '/account')]//p[contains(text(), 'Личный Кабинет')]")  # Ссылка на страницу личного кабинета
REGISTER_PAGE_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")  # Ссылка на страницу регистрации
LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]") # Ссылка в форме регистрации на войти
FORGOT_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]") # Ссылка в форме регистрации на восстановить пароль
BUTTON_RESTORE = (By.CSS_SELECTOR,".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa") #Кнопка восстановить при восстановлении пароля
BUTTON_REGISTRATION = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]") # Кнопка для регистрации
NAME_FIELD = (By.XPATH, "//input[@name='name']")  # Поле для ввода имени
EMAIL_FIELD_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")  # Поле для ввода email на странице входа
EMAIL_FIELD = (By.XPATH, "//div[label[contains(text(), 'Email')]]/input[@name='name']") # Для регистрации
PASSWORD_FIELD_LOGIN = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля на странице входа
REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")  # Сообщение об ошибке при регистрации
LOGIN_BUTTON_MAIN = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка "Войти в аккаунт" на главной странице
LOGIN_BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице входа
PASSWORD_FIELD_PERSONAL_ACCOUNT = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля в личном кабинете
SAVE_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//button[text()='Сохранить']")  # Кнопка "Сохранить" в личном кабинете
CONSTRUCTOR_PERSONAL_ACCOUNT_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка перехода в конструктор в личном кабинете
PASSWORD_FIELD_CONSTRUCTOR = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля в конструкторе
LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__')]")  # Кнопка "Выйти" из личного кабинета
SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Секция "Соусы" в конструкторе
SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок секции "Соусы"
SAUCE_SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']")  # Ингредиент "Соус Spicy-X"
SAUCE_SPACE_SAUCE = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']")  # Ингредиент "Соус фирменный Space Sauce"
SAUCE_GALACTIC = (By.XPATH, "//p[text()='Соус традиционный галактический']")  # Ингредиент "Соус традиционный галактический"
BUTTON_CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]") # Переход по кнопке "конструктор"
BURGER_ELEMENT_TXT = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and contains(text(), 'Соберите бургер')]") #Проверка отображения видимости элемента
HEADER_LOGIN = (By.XPATH, "//h2[text()='Вход']") # Заголовок "Вход"