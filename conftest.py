from distarkcli.utils.MyConfiguration import Configuration
import pytest
import py


confpath = ""

def pytest_addoption(parser):
    parser.addoption("--confpath", action="append", default=[],
                     help="configuration full path")

@py.test.mark.injectconf
@pytest.fixture(scope="session")
def injectconf(request):

    if pytest.config.getoption('confpath') is not None:
        if len(pytest.config.getoption('confpath')) > 0:
            confpath = pytest.config.getoption('confpath')[0]

    print "Launched with conf:", confpath
    Configuration(confpath)
    print "Configuration initialized"



