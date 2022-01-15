import logging
import subprocess
from pyats import aetest
import os
import time


logger = logging.getLogger(__name__)

IP = os.environ['IP']

class tc_one(aetest.Testcase):

    @aetest.setup
    def prepare_testcase(self, section):
        logger.info("Preparing the testttttttttttttttttt")
        logger.info(IP)
        logger.info(section)
        with open('output.json', 'w') as f:
            client_process = subprocess.Popen(['iperf3', '-c', str(IP), '-J'], stdout=f)
        client_process.wait()

    @aetest.test
    def client_launching(self):
        assert 1 == 1


    @aetest.cleanup
    def clean_testcase(self):
        logger.info("Pass testcase cleanup")

# if __name__ == '__main__': # pragma: no cover
#     aetest.main()