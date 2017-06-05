from pyvirtualdisplay import Display
import pytest
import json
import os
import csv
import importlib
from fixture.application import Application
from selenium.webdriver.chrome.webdriver import WebDriver
import logging
import allure


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def app(request):
    global fixture
    global target
    display = Display(visible=0, size=(800, 800))
    display.start()
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    with open(config_file, 'r') as f:
        target = json.load(f)
        fixture = Application(base_url=target['baseUrl'], driver=WebDriver())

    def fin():
        attach = fixture.driver.get_screenshot_as_png()
        if request.node.rep_setup.failed:
            allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(request.function.__name__, attach, allure.attach_type.PNG)
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default='target.json')


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            testdate = load_from_module(fixture[1:])
            metafunc.parametrize(fixture, testdate, ids=[str(x) for x in testdate])
        elif fixture.startswith('csv_'):
            testdate = load_from_csv(fixture[4:])
            metafunc.parametrize(fixture, testdate, ids=[str(x) for x in testdate])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testdate


def load_from_csv(file):
    with open(os.path.join((os.path.dirname((__file__))), 'data/%s.csv' % file), newline='') as csvfile:
        csv_data = csv.DictReader(csvfile)
        data = []
        for row in csv_data:
            data.append(row)
        return data
