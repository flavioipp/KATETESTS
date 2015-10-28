#!/usr/bin/env python
'''
TestCase template for K@TE test developers

[DESCRIPTION]
   Put your test decription here
[DESCRIPTION]
[TOPOLOGY] 1 [TOPOLOGY]
[DEPENDENCY]
   Insert Test dependencies
[DEPENDENCY]
[LAB] Insert the lab referneces i.e. SW,SVT [LAB]
[TPS]
   insert here the Test mapping
[TPS]
[RUNSECTIONS]
   Insert here the sections developed in this test i.e.
   DUTSet,testSet,testBody,testClean,DutClean,all
[RUNSECTIONS]
[AUTHOR] ippolf [AUTHOR]

'''
from KateLibs.testcase import TestCase

class Test(TestCase):
    '''
    this class implements the current test case behaviour by using
    the five methods (runSections):
        DUTSetUp: used for DUT configuration
        testSetup: used for Test Configuration
        testBody: used for main test pourposes
        testCleanUp: used to finalize test and clear the configuration
        DUTCleanUp: used for DUT cleanUp

    all these runSections can be either run or skipped using inline optional input parameters

      --DUTSet     Run the DUTs SetUp
      --testSet    Run the Test SetUp
      --testBody   Run the Test Main Body
      --testClean  Run the Test Clean Up
      --DUTClean   Run the DUTs Clean Up


    without input parameters all runSections will be ran
    '''

    def dut_setup(self):
        print('@Running DUT SetUp...')
        self.report.add_success(None, "Test3 DUT SetUp", '0', "Test3 DUT SetUp Output")

    def test_setup(self):
        print('@Running test Setup...')
        self.report.add_success(None, "test3 SetUp", '0', "Test3 SetUp Output")

    def test_body(self):
        print('@Running Main Test...')
        self.report.start_tps_block('TMPLS', '5-3-22')
        self.report.add_success(None, "comando1_test3", '1', "output comando1 Test3 V2")
        self.report.add_success(None, "comando2_test3", '1', "output comando2")
        self.report.stop_tps_block('TMPLS', '5-3-22')
        self.report.start_tps_block('TMPLS', '5-3-13')
        self.report.add_failure(None, "comando3_test3", '1', "output comando3 TPS V2", "mmm")
        self.report.stop_tps_block('TMPLS', '5-3-13')

    def test_cleanup(self):
        print('@Running Test cleanUp...')
        self.report.add_success(None, "test3 CleanUp", '0', "test3 CleanUp Output")

    def dut_cleanup(self):

        print('@Running DUT cleanUp...')
        self.report.add_success(None, "test3 DUTCleanUp", '0', "test3 DUTCleanUp Output")



#Please don't change the code below

if __name__ == "__main__":
    #initializing the Test object instance and run the main flow
    CTEST = Test(__file__)
    CTEST.run()
