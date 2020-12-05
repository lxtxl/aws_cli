#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details-with-entities.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # job-id : The ID of the request generated by the GenerateServiceLastAccessedDetails operation.
    # service-namespace : The service namespace for an AWS service. Provide the service namespace to learn when the IAM entity last attempted to access the specified service.
To learn the service namespace for a service, go to Actions, Resources, and Condition Keys for AWS Services in the IAM User Guide . Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, (service prefix: a4b) . For more information about service namespaces, see AWS Service Namespaces in the AWS General Reference .
    """

    execute_two_parameter("iam", "get-service-last-accessed-details-with-entities", "job-id", "service-namespace", parameter_display_string)