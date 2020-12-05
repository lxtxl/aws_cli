#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-gov-cloud-account.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # email : The email address of the owner to assign to the new member account in the commercial Region. This email address must not already be associated with another AWS account. You must use a valid email address to complete account creation. You canât access the root user of the account or remove an account that was created with an invalid email address. Like all request parameters for CreateGovCloudAccount , the request for the email address for the AWS GovCloud (US) account originates from the commercial Region, not from the AWS GovCloud (US) Region.
    # account-name : The friendly name of the member account.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "create-gov-cloud-account", "email", "account-name", add_option_dict)
