#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-instance-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-instance-fleets.html
	modify-instance-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-fleet.html
    """

    write_parameter("emr", "add-instance-fleet")