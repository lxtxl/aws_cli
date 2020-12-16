#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	assign-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-instance.html
	delete-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-instance.html
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-instance.html
	describe-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-instances.html
	reboot-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/reboot-instance.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-instance.html
	start-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-instance.html
	stop-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-instance.html
	unassign-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-instance.html
	update-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-instance.html
    """

    write_parameter("opsworks", "create-instance")