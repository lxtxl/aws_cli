#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/delete-db-instance.html
	describe-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-db-instances.html
	modify-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/modify-db-instance.html
	reboot-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/reboot-db-instance.html
    """

    write_parameter("neptune", "create-db-instance")