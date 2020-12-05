#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/describe-permission-set-provisioning-status.html
if __name__ == '__main__':
    """
	list-permission-set-provisioning-status : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/list-permission-set-provisioning-status.html
    """

    parameter_display_string = """
    # instance-arn : The ARN of the SSO instance under which the operation will be executed. For more information about ARNs, see Amazon Resource Names (ARNs) and AWS Service Namespaces in the AWS General Reference .
    # provision-permission-set-request-id : The identifier that is provided by the  ProvisionPermissionSet call to retrieve the current status of the provisioning workflow.
    """

    execute_two_parameter("sso-admin", "describe-permission-set-provisioning-status", "instance-arn", "provision-permission-set-request-id", parameter_display_string)