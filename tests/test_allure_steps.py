import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_dynamic_steps():
    allure.dynamic.tag("github")
    allure.dynamic.label("owner", 'aistabk')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature("Проверка наличия Issues в репозитории")
    allure.dynamic.story("Как пользователь я хочу видеть в репозитории созданные ранее issues")
    allure.dynamic.link("https://github.com", name="Testing")

    with allure.step("Найти репозиторий через поиск"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("aistabk/qa_guru_8_9")
        s("#query-builder-test").submit()

    with allure.step("Перейти в репозиторий"):
        s(by.link_text("aistabk/qa_guru_8_9")).click()

    with allure.step("Открыть вкладку Issues"):
        s("#issues-tab").click()

    with allure.step("Проверить наличие Issue с именем issue for test"):
        s(by.partial_text("issue for test")).should(be.visible)
