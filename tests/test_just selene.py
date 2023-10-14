
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_just_selene():
    s(".search-input").click()
    s("#query-builder-test").send_keys("aistabk/qa_guru_8_9")
    s("#query-builder-test").submit()
    s(by.link_text("aistabk/qa_guru_8_9")).click()
    s("#issues-tab").click()
    s(by.partial_text("issue for test")).should(be.visible)

