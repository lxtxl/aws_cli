#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/add-notification-channels.html
if __name__ == '__main__':
    """
	remove-notification-channel : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/remove-notification-channel.html
    """

    parameter_display_string = """
    # channels : One or 2 channels to report to when anomalies are detected.
(structure)

Notification medium for users to get alerted for events that occur in application profile. We support SNS topic as a notification channel.
eventPublishers -> (list)

List of publishers for different type of events that may be detected in an application from the profile. Anomaly detection is the only event publisher in Profiler.
(string)

id -> (string)

Unique identifier for each Channel in the notification configuration of a Profiling Group. A random UUID for channelId is used when adding a channel to the notification configuration if not specified in the request.

uri -> (string)

Unique arn of the resource to be used for notifications. We support a valid SNS topic arn as a channel uri.
    # profiling-group-name : The name of the profiling group that we are setting up notifications for.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("codeguruprofiler", "add-notification-channels", "channels", "profiling-group-name", add_option_dict)
