import logging
import subprocess
import time
logger = logging.getLogger(__name__)


logger.info("Preparing the test")
  
server = subprocess.Popen(['iperf3' , '-s', '--one-off'])
time.sleep(300)

logger.info("Pass testcase cleanup")

# if __name__ == '__main__': # pragma: no cover
#     aetest.main()