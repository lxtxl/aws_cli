#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaign.html
if __name__ == '__main__':
    """
	create-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-campaign.html
	delete-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-campaign.html
	get-campaigns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaigns.html
	update-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-campaign.html
    """

    parameter_display_string = """
    # application-id : The unique identifier for the application. This identifier is displayed as the Project ID on the Amazon Pinpoint console.
    # campaign-id : The unique identifier for the campaign.
    """

    execute_two_parameter("pinpoint", "get-campaign", "application-id", "campaign-id", parameter_display_string)