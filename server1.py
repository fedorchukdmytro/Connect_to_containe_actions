import logging
import subprocess

logger = logging.getLogger(__name__)


logger.info("Preparing the test")
  
server = subprocess.Popen(['iperf3' , '-s', '--one-off'])

logger.info("Pass testcase cleanup")

# if __name__ == '__main__': # pragma: no cover
#     aetest.main()