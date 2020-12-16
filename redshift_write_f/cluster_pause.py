#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html
	delete-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html
	describe-clusters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html
	modify-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html
	reboot-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html
	resize-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resize-cluster.html
	resume-cluster : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resume-cluster.html
    """

    write_parameter("redshift", "pause-cluster")