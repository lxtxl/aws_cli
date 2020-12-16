#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-instance.html
	describe-db-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instances.html
	modify-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-instance.html
	reboot-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-instance.html
	start-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-instance.html
	stop-db-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-instance.html
    """

    write_parameter("rds", "create-db-instance")