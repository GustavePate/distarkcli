from distarkcli.services.searchfoodservice import SearchFoodServiceFactory
from distarkcli.services.searchfoodservice import SearchFoodRequest
import py
import pytest

@pytest.mark.usefixtures("injectconf")
class TestSearchFoodService(object):

    @py.test.mark.injectconf
    def test_searchfoodservice(self):
        self.callsearchfoodservice()

    def callsearchfoodservice(self, txtreq='youpi'):
        request = SearchFoodRequest()
        request.setReq(txtreq)
        ss = SearchFoodServiceFactory(request)
        # blocking call
        response = ss.getResponse()
        if response[0] == ss.pbresptype:
            assert len(response[1].getFoods()) == 4
        else:
            assert 0
