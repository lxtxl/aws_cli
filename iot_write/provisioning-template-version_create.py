#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template-version.html
	describe-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template-version.html
	list-provisioning-template-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-template-versions.html
    """

    write_parameter("iot", "create-provisioning-template-version")