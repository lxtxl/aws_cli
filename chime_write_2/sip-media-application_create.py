#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-media-application.html
if __name__ == '__main__':
    """
	delete-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-sip-media-application.html
	get-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-media-application.html
	list-sip-media-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-media-applications.html
	update-sip-media-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-sip-media-application.html
    """

    parameter_display_string = """
    # aws-region : AWS Region assigned to the SIP media application.
    # endpoints : List of endpoints (Lambda Amazon Resource Names) specified for the SIP media application. Currently, only one endpoint is supported.
(structure)

Endpoints to specify as part of a SIP media application.
LambdaArn -> (string)

Valid Amazon Resource Name (ARN) of the Lambda function of the same AWS Region where the SIP media application is created.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "create-sip-media-application", "aws-region", "endpoints", add_option_dict)
