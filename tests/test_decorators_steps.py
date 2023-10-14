import allure
from selene.support import by
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("github")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "aistabk")
@allure.feature("Проверка наличия Issues в репозитории")
@allure.story("Как пользователь я хочу видеть в репозитории созданные ранее issues")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    search_for_repository("aistabk/qa_guru_8_9")
    go_to_repository("aistabk/qa_guru_8_9")
    open_issue_tab()
    should_see_issue_with_number("issue for test")


@allure.step("Найти репозиторий {repo} через поиск")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys("aistabk/qa_guru_8_9")
    s("#query-builder-test").submit()


@allure.step("Перейти в репозиторий {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открыть вкладку Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверить наличие Issue с именем issue for test")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
