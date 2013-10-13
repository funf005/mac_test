#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
from time import sleep
from ConfigParser import SafeConfigParser

class jobData:
    jobStatus = {}
    
    def __init__(self):
        config = SafeConfigParser()
        config.read('test.ini')
        for job in config.sections():
            list = [config.get(job,'job_script'),config.get(job,'job_waits').split(','),'',-1]
            self.jobStatus.update({job:list})
        
    #TODO 次に実行するジョブIDを算出する関数を追加する。引数：void 戻り値：List
    def nextFireJobs(self):
        nonRunningJobs = nonRunnningJobs()
        for job in nonRunningJobs:
            waitList = self.jobStatus[job][1]
            for waitJob in waitList:
            #waitListの中のジョブがnonRunnnigJobsの中になかったら    
    
    #TODO 実行失敗したジョブリストを返す。引数：void 戻り値：List
    def failedJobs(self):
        jobList= []
        for job in self.jobStatus:
            if(self.jobStatus[job][2] == 'failed')
                jobList.append(job)
        return jobList
            
    #TODO まだ実行されていないジョブを算出する関数を追加する。引数：void 戻り値：List
    def nonRunningJobs(self):
        jobList = []
        for job in self.jobStatus:
            if(self.jobStatus[job][2] != -1):
                jobList.append(job)
        return jobList

def jobkicker(self):
   sleep(2) 


if __name__ == '__main__':
    print "aaaaaa"
    j = jobData();
    j.nonRunningJobs()
    
