import pytest
import chromedriver_autoinstaller
import selenium.webdriver

chromedriver_autoinstaller.install()

@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()

    b.implicitly_wait(10)

    yield b

    b.quit()