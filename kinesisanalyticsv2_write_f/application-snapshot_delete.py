#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-application-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/create-application-snapshot.html
	describe-application-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/describe-application-snapshot.html
	list-application-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/list-application-snapshots.html
    """

    write_parameter("kinesisanalyticsv2", "delete-application-snapshot")