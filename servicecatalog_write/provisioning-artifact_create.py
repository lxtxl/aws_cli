#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioning-artifact.html
	describe-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html
	list-provisioning-artifacts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioning-artifacts.html
	update-provisioning-artifact : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html
    """

    write_parameter("servicecatalog", "create-provisioning-artifact")