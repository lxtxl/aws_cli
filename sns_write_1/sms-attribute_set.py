#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-sms-attributes.html
if __name__ == '__main__':
    """
	get-sms-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-sms-attributes.html
    """

    parameter_display_string = """
    # attributes : The default settings for sending SMS messages from your account. You can set values for the following attribute names:

MonthlySpendLimit â The maximum amount in USD that you are willing to spend each month to send SMS messages. When Amazon SNS determines that sending an SMS message would incur a cost that exceeds this limit, it stops sending SMS messages within minutes.


Warning
Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During that interval, if you continue to send SMS messages, you will incur costs that exceed your limit.

By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to raise the limit, submit an SNS Limit Increase case . For New limit value , enter your desired monthly spend limit. In the Use Case Description field, explain that you are requesting an SMS monthly spend limit increase.

DeliveryStatusIAMRole â The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS writes a log that includes the message price, the success or failure status, the reason for failure (if the message failed), the message dwell time, and other information.
DeliveryStatusSuccessSamplingRate â The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 - 100. For example, to write logs only for failed deliveries, set this value to 0 . To write logs for 10% of your successful deliveries, set it to 10 .
DefaultSenderID â A string, such as your business brand, that is displayed as the sender on the receiving device. Support for sender IDs varies by country. The sender ID can be 1 - 11 alphanumeric characters, and it must contain at least one letter.
DefaultSMSType â The type of SMS message that you will send by default. You can assign the following values:


Promotional â (Default) Noncritical messages, such as marketing messages. Amazon SNS optimizes the message delivery to incur the lowest cost.
Transactional â Critical messages that support customer transactions, such as one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message delivery to achieve the highest reliability.


UsageReportS3Bucket â The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file to the bucket. The report includes the following information for each SMS message that was successfully delivered by your account:


Time that the message was published (in UTC)
Message ID
Destination phone number
Message type
Delivery status
Message price (in USD)
Part number (a message is split into multiple parts if it is too long for a single message)
Total number of parts

To receive the report, the bucket must have a policy that allows the Amazon SNS service principle to perform the s3:PutObject and s3:GetBucketLocation actions.
For an example bucket policy and usage report, see Monitoring SMS Activity in the Amazon SNS Developer Guide .
key -> (string)
value -> (string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sns", "set-sms-attributes", "attributes", add_option_dict)





