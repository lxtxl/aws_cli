#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-attached-policies.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # target : The group or principal for which the policies will be listed. Valid principals are CertificateArn (arn:aws:iot:region :accountId :cert/certificateId ), thingGroupArn (arn:aws:iot:region :accountId :thinggroup/groupName ) and CognitoId (region :id ).
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("iot", "list-attached-policies", "target", add_option_dict)