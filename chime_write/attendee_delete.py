#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-attendee.html
	get-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-attendee.html
	list-attendees : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-attendees.html
	tag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/tag-attendee.html
	untag-attendee : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/untag-attendee.html
    """

    write_parameter("chime", "delete-attendee")