#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/associate-fleet.html
	create-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/create-fleet.html
	delete-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/delete-fleet.html
	describe-fleets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-fleets.html
	disassociate-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/disassociate-fleet.html
	stop-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/stop-fleet.html
	update-fleet : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/update-fleet.html
    """

    write_parameter("appstream", "start-fleet")