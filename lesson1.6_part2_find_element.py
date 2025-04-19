from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")

"""
find_element(By.ID, value) — поиск по уникальному атрибуту id элемента. 
Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, 
и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS. 
Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и 
задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, 
то скорее всего вы будете использовать именно этот метод в ваших тестах;
find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень 
гибкий поиск элементов;
find_element(By.NAME, value) — поиск по атрибуту name элемента;
find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора 
совпадает с любой частью текста ссылки.
"""