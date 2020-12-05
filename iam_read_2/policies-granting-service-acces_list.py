#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policies-granting-service-access.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # arn : The ARN of the IAM identity (user, group, or role) whose policies you want to list.
    # service-namespaces : The service namespace for the AWS services whose policies you want to list.
To learn the service namespace for a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .
(string)
    """

    execute_two_parameter("iam", "list-policies-granting-service-access", "arn", "service-namespaces", parameter_display_string)