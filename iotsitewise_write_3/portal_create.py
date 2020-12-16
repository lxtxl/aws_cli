#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-portal.html
if __name__ == '__main__':
    """
	delete-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-portal.html
	describe-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html
	list-portals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-portals.html
	update-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html
    """

    parameter_display_string = """
    # portal-name : A friendly name for the portal.
    # portal-contact-email : The AWS administratorâs contact email address.
    # role-arn : The ARN of a service role that allows the portalâs users to access your AWS IoT SiteWise resources on your behalf. For more information, see Using service roles for AWS IoT SiteWise Monitor in the AWS IoT SiteWise User Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("iotsitewise", "create-portal", "portal-name", "portal-contact-email", "role-arn", add_option_dict)
