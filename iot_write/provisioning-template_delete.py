#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template.html
	describe-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template.html
	list-provisioning-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-templates.html
	update-provisioning-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-provisioning-template.html
    """

    write_parameter("iot", "delete-provisioning-template")