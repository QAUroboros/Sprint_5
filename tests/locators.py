from selenium.webdriver.common.by import By


LOGIN_PAGE_LINK = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")  # Ссылка на страницу личного кабинета
REGISTER_PAGE_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']/p[text()='Зарегистрироваться']")  # Ссылка на страницу регистрации
NAME_FIELD = (By.XPATH, "//input[@name='name']")  # Поле для ввода имени
EMAIL_FIELD = (By.XPATH, "//input[@name='email']")  # Поле для ввода email
PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")  # Поле для ввода пароля
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
REGISTRATION_ERROR_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Сообщение об ошибке при регистрации
LOGIN_BUTTON_MAIN = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка "Войти" на главной странице
EMAIL_FIELD_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")  # Поле для ввода email на странице входа
PASSWORD_FIELD_LOGIN = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля на странице входа
LOGIN_BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице входа
PERSONAL_ACCOUNT_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка перехода в личный кабинет
EMAIL_FIELD_PERSONAL_ACCOUNT = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")  # Поле для ввода email в личном кабинете
PASSWORD_FIELD_PERSONAL_ACCOUNT = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля в личном кабинете
SAVE_BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//button[text()='Сохранить']")  # Кнопка "Сохранить" в личном кабинете
CONSTRUCTOR_PERSONAL_ACCOUNT_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")  # Кнопка перехода в конструктор в личном кабинете
EMAIL_FIELD_CONSTRUCTOR = (By.XPATH, "//div[contains(@class, 'input_type_text')]//input[@name='name']")  # Поле для ввода email в конструкторе
PASSWORD_FIELD_CONSTRUCTOR = (By.XPATH, "//input[@name='Пароль']")  # Поле для ввода пароля в конструкторе
LOGIN_BUTTON_CONSTRUCTOR = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" в конструкторе
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")  # Кнопка "Выйти" из личного кабинета
SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Секция "Соусы" в конструкторе
SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок секции "Соусы"
SAUCE_SPICY_X = (By.XPATH, "//p[text()='Соус Spicy-X']")  # Ингредиент "Соус Spicy-X"
SAUCE_SPACE_SAUCE = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']")  # Ингредиент "Соус фирменный Space Sauce"
SAUCE_GALACTIC = (By.XPATH, "//p[text()='Соус традиционный галактический']")  # Ингредиент "Соус традиционный галактический"
