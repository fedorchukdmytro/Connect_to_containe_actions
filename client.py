import logging
import subprocess
from pyats import aetest
import os

# IP = os.getenv['IP']

logger = logging.getLogger(__name__)

class tc_one(aetest.Testcase):

    @aetest.setup
    def prepare_testcase(self, section):
        logger.info("Preparing the test")
        logger.info(section)

    @aetest.test
    def client_launching(self):
        with open('output.json', 'w') as f:
            client_process = subprocess.Popen(['iperf3', '-c', '10.1.0.1', '-p', '5201' '-J'], stdout=f,)
        client_process.wait()

    @aetest.cleanup
    def clean_testcase(self):
        logger.info("Pass testcase cleanup")

# if __name__ == '__main__': # pragma: no cover
#     aetest.main()