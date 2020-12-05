#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/get-cloud-formation-template.html
if __name__ == '__main__':
    """
	create-cloud-formation-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-template.html
    """

    parameter_display_string = """
    # application-id : The Amazon Resource Name (ARN) of the application.
    # template-id : The UUID returned by CreateCloudFormationTemplate.
Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}
    """

    execute_two_parameter("serverlessrepo", "get-cloud-formation-template", "application-id", "template-id", parameter_display_string)