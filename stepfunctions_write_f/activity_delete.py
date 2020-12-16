#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-activity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-activity.html
	describe-activity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-activity.html
	list-activities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-activities.html
    """

    write_parameter("stepfunctions", "delete-activity")