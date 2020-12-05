#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details-for-organization.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # organization-event-detail-filters : A set of JSON elements that includes the awsAccountId and the eventArn .
(structure)

The values used to filter results from the DescribeEventDetailsForOrganization and DescribeAffectedEntitiesForOrganization operations.
eventArn -> (string)

The unique identifier for the event. Format: arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` . Example: ``Example: arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456

awsAccountId -> (string)

The 12-digit AWS account numbers that contains the affected entities.
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

    execute_one_parameter("health", "describe-event-details-for-organization", "organization-event-detail-filters", add_option_dict)