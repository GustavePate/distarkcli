from distarkcli.services.simpleservice import SimpleServiceFactory
from distarkcli.services.simpleservice import SimpleRequest
import py
import pytest

@pytest.mark.usefixtures("injectconf")
class TestSimpleService(object):

    @py.test.mark.injectconf
    def test_simpleservice(self):
        self.callsimpleservice()

    def callsimpleservice(self, txtreq='anotherworld'):
        request = SimpleRequest()
        request.setYoupla(txtreq)
        ss = SimpleServiceFactory(request)
        # blocking call
        response = ss.getResponse()
        if response[0] == ss.pbresptype:
            assert response[1].getBoum() == ''.join(reversed(txtreq))
        else:
            assert 0
