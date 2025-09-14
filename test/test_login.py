# tests/test_login.py
from pages.login_page import LoginPage
import pytest

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    # Aquí puedes agregar una verificación, por ejemplo, que el URL cambió.
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_failed_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("wrong_user", "wrong_password")
    # Aquí puedes verificar que el mensaje de error aparece.
    assert login_page.error_message.is_visible()