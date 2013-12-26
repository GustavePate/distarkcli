
from distarkcli.services.simpleservice import SimpleService
from distarkcli.services.simpleservice import SimpleRequest
from distarkcli.utils.MyConfiguration import Configuration

import argparse
import traceback


class TestSimpleService(object):

    def test_simpleservice(self):
        self.callsimpleservice()

    def callsimpleservice(self, txtreq='anotherworld'):
        request = SimpleRequest()
        request.setYoupla(txtreq)
        ss = SimpleService(request)
        # blocking call
        response = ss.getResponse()
        if response[0] == ss.pbresptype:
            assert response[1].getBoum() == ''.join(reversed(txtreq))
        else:
            assert 0

if __name__ == '__main__':

    ##############################################
    #     ARGUMENTS PARSING
    ##############################################
    parser = argparse.ArgumentParser(description='Send requests')
    parser.add_argument('conf',
                        help='conf filepath',
                        type=str)
    args = parser.parse_args()
    print "Program Launched with args:" + str(args)
    print "Do:" + str(args.conf)
    conf = Configuration(args.conf)

    try:
        test = TestSimpleService()
        test.callsimpleservice()
    except:
        traceback.print_exc()
