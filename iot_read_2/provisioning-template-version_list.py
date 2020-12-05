#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template-version.html
if __name__ == '__main__':
    """
	create-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template-version.html
	delete-provisioning-template-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template-version.html
	list-provisioning-template-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-template-versions.html
    """

    parameter_display_string = """
    # template-name : The template name.
    # version-id : The fleet provisioning template version ID.
    """

    execute_two_parameter("iot", "describe-provisioning-template-version", "template-name", "version-id", parameter_display_string)