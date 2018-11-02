__author__ = 'mihung'


''' Commands to run pyats

From YOUR local machine:

       $ ssh rhetting@csaf-pitt-2.cisco.com

See what shell is running (source env.sh   ->   source.csh)

       $ echo $SHELL
       $ bash

Switch to the ATS Training Environment

  $ cd /csaf_auto/pyATS3
  $ source env.sh

  (pyATS3) $ python --version
  (pyATS3) $ git --version
  (pyATS3) $ ipython
       import yaml
       import ats
       quit

  (pyATS3) $ cd atseasy
  (pyATS3) $ source tcl_on.sh

  (pyATS3) $ pwd                                # verify you are in atseasy
  (pyATS3) $ mkdir yourname                     # YOUR ID GOES HERE
  (pyATS3) $ cd yourname                        # YOUR ID GOES HERE

  (pyATS3) $ mkdir etc
  (pyATS3) $ mkdir tests
  (pyATS3) $ mkdir jobs

  (pyATS3) $ cp ../rhett11/etc/pyclass.yaml etc
  (pyATS3) $ cp ../rhett11/tests/show_ver_test.py tests
  (pyATS3) $ cp ../rhett11/jobs/show_ver_job.py jobs


  Standalone:
  -----------
  (pyATS3) $ cd tests
  (pyATS3) $ python show_ver_test.py

  Part of the full test system (email, TIMS, Trade, Archive, etc):
  ----------------------------------------------------------------
  (pyATS3) $ cd ../jobs
  (pyATS3) $ easypy show_ver_job.py

  How do I check-in?
  ------------------

'''

