#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/associate-drt-role.html
if __name__ == '__main__':
    """
	disassociate-drt-role : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/disassociate-drt-role.html
    """

    parameter_display_string = """
    # role-arn : The Amazon Resource Name (ARN) of the role the DRT will use to access your AWS account.
Prior to making the AssociateDRTRole request, you must attach the AWSShieldDRTAccessPolicy managed policy to this role. For more information see `Attaching and Detaching IAM Policies < https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`__ .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("shield", "associate-drt-role", "role-arn", add_option_dict)





