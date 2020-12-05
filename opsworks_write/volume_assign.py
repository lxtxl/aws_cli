#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-volume.html
	describe-volumes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-volumes.html
	register-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-volume.html
	unassign-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-volume.html
	update-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-volume.html
    """

    write_parameter("opsworks", "assign-volume")