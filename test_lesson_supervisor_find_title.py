"""Поиск заголовка в Супервайзере"""

import pytest
from pytest_bdd import (given, scenario, then, when, parsers)
from BddAcceptanceTests.tests.utils.pageobjects.supervisor.DashboardsPage import DashboardsPage


@pytest.fixture(scope='function')
def dashboards_page(browser):
    return DashboardsPage(browser)


@pytest.mark.supervisor
@pytest.mark.nmgk
@pytest.mark.mytest_1
@scenario('../../../features/supervisor/common/lesson_supervisor_find_title.feature', 'Поиск заголовка в теге title на странице Дашборды')
def test_open_dashboards_to_find_title():
    """Поиск заголовка в теге title на странице Дашборды"""


@given('Открыта страница Дашбордов')
def supervisor_is_opened(dashboards_page):
    """Открыта страница Дашбордов"""
    dashboards_page.go_to_page()


@then(parsers.parse('Заголовок в теге title == {search_title}'))
def first_title_on_page(dashboards_page, search_title):
    """Заголовок в теге h2 == ST Супервайзер - Панель индикаторов (Рубаненко Рустам Игоревич)"""
    assert dashboards_page.find_tag_with_text('title', search_title), f'{search_title} is not shown'

