#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-campaign.html
if __name__ == '__main__':
    """
	delete-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-campaign.html
	describe-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-campaign.html
	list-campaigns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-campaigns.html
	update-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/update-campaign.html
    """

    parameter_display_string = """
    # name : A name for the new campaign. The campaign name must be unique within your account.
    # solution-version-arn : The Amazon Resource Name (ARN) of the solution version to deploy.
    # min-provisioned-tps : Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("personalize", "create-campaign", "name", "solution-version-arn", "min-provisioned-tps", add_option_dict)
