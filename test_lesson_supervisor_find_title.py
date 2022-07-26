"""Поиск заголовка в Супервайзере"""

import pytest
from pytest_bdd import (given, scenario, then, when, parsers)
from BddAcceptanceTests.tests.utils.pageobjects.supervisor.BaseSupervisorPage import BaseSupervisorPage
from BddAcceptanceTests.tests.utils.pageobjects.supervisor.DashboardsPage import DashboardsPage


@pytest.fixture(scope='function')
def base_supervisor_page(browser):
    return DashboardsPage(browser)


@pytest.mark.supervisor
@pytest.mark.nmgk
@pytest.mark.mytest_1
@scenario('../../../features/supervisor/common/lesson_supervisor_find_title.feature', 'Поиск заголовка в теге title на странице Дашборды')
def test_open_dashboards_to_find_title():
    """Поиск заголовка в теге title на странице Дашборды"""


@given('Открыта страница Дашбордов')
def supervisor_is_opened(base_supervisor_page):
    """Открыта страница Дашбордов"""
    base_supervisor_page.go_to_page()


@then(parsers.parse('Заголовок в теге title == {search_title}'))
def first_title_on_page(supervisor_dashboard_page, search_title):
    """Заголовок в теге h2 == ST Супервайзер - Панель индикаторов (Рубаненко Рустам Игоревич)"""
    assert supervisor_dashboard_page.find_tag_with_text('title', search_title), f'{search_title} is not shown'

