#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-mitigation-action.html
	delete-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-mitigation-action.html
	describe-mitigation-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-mitigation-action.html
	list-mitigation-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-mitigation-actions.html
    """

    write_parameter("iot", "update-mitigation-action")