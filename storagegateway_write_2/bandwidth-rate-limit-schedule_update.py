#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/update-bandwidth-rate-limit-schedule.html
if __name__ == '__main__':
    """
	describe-bandwidth-rate-limit-schedule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-bandwidth-rate-limit-schedule.html
    """

    parameter_display_string = """
    # gateway-arn : The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and AWS Region.
    # bandwidth-rate-limit-intervals : An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty.
(structure)

Describes a bandwidth rate limit interval for a gateway. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both.
StartHourOfDay -> (integer)

The hour of the day to start the bandwidth rate limit interval.

StartMinuteOfHour -> (integer)

The minute of the hour to start the bandwidth rate limit interval. The interval begins at the start of that minute. To begin an interval exactly at the start of the hour, use the value 0 .

EndHourOfDay -> (integer)

The hour of the day to end the bandwidth rate limit interval.

EndMinuteOfHour -> (integer)

The minute of the hour to end the bandwidth rate limit interval.

Warning
The bandwidth rate limit interval ends at the end of the minute. To end an interval at the end of an hour, use the value 59 .


DaysOfWeek -> (list)

The days of the week component of the bandwidth rate limit interval, represented as ordinal numbers from 0 to 6, where 0 represents Sunday and 6 Saturday.
(integer)

AverageUploadRateLimitInBitsPerSec -> (long)

The average upload rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the upload rate limit is not set.

AverageDownloadRateLimitInBitsPerSec -> (long)

The average download rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the download rate limit is not set.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("storagegateway", "update-bandwidth-rate-limit-schedule", "gateway-arn", "bandwidth-rate-limit-intervals", add_option_dict)
