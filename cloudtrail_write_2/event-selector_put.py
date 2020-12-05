#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html
if __name__ == '__main__':
    """
	get-event-selectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-selectors.html
    """

    parameter_display_string = """
    # trail-name : Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:

Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)
Start with a letter or number, and end with a letter or number
Be between 3 and 128 characters
Have no adjacent periods, underscores or dashes. Names like my-_namespace and my--namespace are invalid.
Not be in IP address format (for example, 192.168.5.4)

If you specify a trail ARN, it must be in the format:

arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail
    # event-selectors : Specifies the settings for your event selectors. You can configure up to five event selectors for a trail.
(structure)

Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesnât match any event selector, the trail doesnât log the event.
You can configure up to five event selectors for a trail.
ReadWriteType -> (string)

Specify if you want your trail to log read-only events, write-only events, or all. For example, the EC2 GetConsoleOutput is a read-only API operation and RunInstances is a write-only API operation.
By default, the value is All .

IncludeManagementEvents -> (boolean)

Specify if you want your event selector to include management events for your trail.
For more information, see Management Events in the AWS CloudTrail User Guide .
By default, the value is true .

DataResources -> (list)

CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions. You can specify up to 250 resources for an individual event selector, but the total number of data resources cannot exceed 250 across all event selectors in a trail. This limit does not apply if you configure resource logging for all data events.
For more information, see Data Events and Limits in AWS CloudTrail in the AWS CloudTrail User Guide .
(structure)

The Amazon S3 buckets or AWS Lambda functions that you specify in your event selectors for your trail to log data events. Data events provide information about the resource operations performed on or within a resource itself. These are also known as data plane operations. You can specify up to 250 data resources for a trail.

Note
The total number of allowed data resources is 250. This number can be distributed between 1 and 5 event selectors, but the total cannot exceed 250 across all selectors.

The following example demonstrates how logging works when you configure logging of all data events for an S3 bucket named bucket-1 . In this example, the CloudTrail user specified an empty prefix, and the option to log both Read and Write data events.

A user uploads an image file to bucket-1 .
The PutObject API operation is an Amazon S3 object-level API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3 bucket with an empty prefix, events that occur on any object in that bucket are logged. The trail processes and logs the event.
A user uploads an object to an Amazon S3 bucket named arn:aws:s3:::bucket-2 .
The PutObject API operation occurred for an object in an S3 bucket that the CloudTrail user didnât specify for the trail. The trail doesnât log the event.

The following example demonstrates how logging works when you configure logging of AWS Lambda data events for a Lambda function named MyLambdaFunction , but not for all AWS Lambda functions.

A user runs a script that includes a call to the MyLambdaFunction function and the MyOtherLambdaFunction function.
The Invoke API operation on MyLambdaFunction is an AWS Lambda API. It is recorded as a data event in CloudTrail. Because the CloudTrail user specified logging data events for MyLambdaFunction , any invocations of that function are logged. The trail processes and logs the event.
The Invoke API operation on MyOtherLambdaFunction is an AWS Lambda API. Because the CloudTrail user did not specify logging data events for all Lambda functions, the Invoke operation for MyOtherLambdaFunction does not match the function specified for the trail. The trail doesnât log the event.

Type -> (string)

The resource type in which you want to log data events. You can specify AWS::S3::Object or AWS::Lambda::Function resources.

Values -> (list)

An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified objects.

To log data events for all objects in all S3 buckets in your AWS account, specify the prefix as arn:aws:s3::: .


Note
This will also enable logging of data event activity performed by any user or role in your AWS account, even if that activity is performed on a bucket that belongs to another AWS account.


To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as arn:aws:s3:::bucket-1/ . The trail logs data events for all objects in this S3 bucket.
To log data events for specific objects, specify the S3 bucket and object prefix such as arn:aws:s3:::bucket-1/example-images . The trail logs data events for objects in this S3 bucket that match the prefix.
To log data events for all functions in your AWS account, specify the prefix as arn:aws:lambda .


Note
This will also enable logging of Invoke activity performed by any user or role in your AWS account, even if that activity is performed on a function that belongs to another AWS account.


To log data events for a specific Lambda function, specify the function ARN.


Note
Lambda function ARNs are exact. For example, if you specify a function ARN arn:aws:lambda:us-west-2:111111111111:function:helloworld , data events will only be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld . They will not be logged for arn:aws:lambda:us-west-2:111111111111:function:helloworld2 .

(string)



ExcludeManagementEventSources -> (list)

An optional list of service event sources from which you do not want management events to be logged on your trail. In this release, the list can be empty (disables the filter), or it can filter out AWS Key Management Service events by containing "kms.amazonaws.com" . By default, ExcludeManagementEventSources is empty, and AWS KMS events are included in events that are logged to your trail.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudtrail", "put-event-selectors", "trail-name", "event-selectors", add_option_dict)
