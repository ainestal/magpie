"""
magpie.aws.emr
============
The AWS EMR inventory class
"""
from boto.emr.connection import EmrConnection
from boto.ec2.regioninfo import RegionInfo

class EMRInventory():
    def __init__(self, region='eu-west-1'):
        regionEMR = self.get_emr_region(region)
        self.emrConnection = EmrConnection(region=regionEMR)

    def list_current_resources(self, region='eu-west-1'):
        jobFlows = self.emrConnection.describe_jobflows()
        for jobFlow in jobFlows:
            print jobFlow.jobflowid

    def get_emr_region(self, region='eu-west-1'):
        regionEndpoint = '%s.elasticmapreduce.amazonaws.com' % region
        regionEMR = RegionInfo (name=region,
                                endpoint=regionEndpoint)
        return regionEMR
