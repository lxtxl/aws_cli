#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-campaign.html
	get-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaign.html
	get-campaigns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaigns.html
	update-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-campaign.html
    """

    write_parameter("pinpoint", "create-campaign")