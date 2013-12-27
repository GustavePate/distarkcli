from distarkcli.services.anotherservice import AnotherServiceFactory
from distarkcli.services.anotherservice import AnotherRequest
import py
import pytest

@pytest.mark.usefixtures("injectconf")
class TestAnotherService(object):

    @py.test.mark.injectconf
    def test_anotherservice(self):
        self.callanotherservice()

    def callanotherservice(self, txtreq='anotherworld'):
        request = AnotherRequest()
        request.setRequestStr(txtreq)
        ss = AnotherServiceFactory(request)
        # blocking call
        response = ss.getResponse()
        if response[0] == ss.pbresptype:
            assert response[1].getResponseStr() == ''.join([txtreq, txtreq])
        else:
            assert 0
