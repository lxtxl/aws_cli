#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-campaign.html
	delete-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-campaign.html
	describe-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-campaign.html
	list-campaigns : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-campaigns.html
    """

    write_parameter("personalize", "update-campaign")