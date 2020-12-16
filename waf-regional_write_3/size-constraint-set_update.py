#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html
if __name__ == '__main__':
    """
	create-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-size-constraint-set.html
	delete-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-size-constraint-set.html
	get-size-constraint-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-size-constraint-set.html
	list-size-constraint-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-size-constraint-sets.html
    """

    parameter_display_string = """
    # size-constraint-set-id : The SizeConstraintSetId of the  SizeConstraintSet that you want to update. SizeConstraintSetId is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    # updates : An array of SizeConstraintSetUpdate objects that you want to insert into or delete from a  SizeConstraintSet . For more information, see the applicable data types:

SizeConstraintSetUpdate : Contains Action and SizeConstraint
SizeConstraint : Contains FieldToMatch , TextTransformation , ComparisonOperator , and Size
FieldToMatch : Contains Data and Type

(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


Specifies the part of a web request that you want to inspect the size of and indicates whether you want to add the specification to a  SizeConstraintSet or delete it from a SizeConstraintSet .
Action -> (string)

Specify INSERT to add a  SizeConstraintSetUpdate to a  SizeConstraintSet . Use DELETE to remove a SizeConstraintSetUpdate from a SizeConstraintSet .

SizeConstraint -> (structure)

Specifies a constraint on the size of a part of the web request. AWS WAF uses the Size , ComparisonOperator , and FieldToMatch to build an expression in the form of âSize ComparisonOperator size in bytes of FieldToMatch â. If that expression is true, the SizeConstraint is considered to match.
FieldToMatch -> (structure)

Specifies where in a web request to look for the size constraint.
Type -> (string)

The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

HEADER : A specified request header, for example, the value of the User-Agent or Referer header. If you choose HEADER for the type, specify the name of the header in Data .
METHOD : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: DELETE , GET , HEAD , OPTIONS , PATCH , POST , and PUT .
QUERY_STRING : A query string, which is the part of a URL that appears after a ? character, if any.
URI : The part of a web request that identifies a resource, for example, /images/daily-ad.jpg .
BODY : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first 8192 bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
SINGLE_QUERY_ARG : The parameter in the query string that you will inspect, such as UserName or SalesRegion . The maximum length for SINGLE_QUERY_ARG is 30 characters.
ALL_QUERY_ARGS : Similar to SINGLE_QUERY_ARG , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in TargetString .


Data -> (string)

When the value of Type is HEADER , enter the name of the header that you want AWS WAF to search, for example, User-Agent or Referer . The name of the header is not case sensitive.
When the value of Type is SINGLE_QUERY_ARG , enter the name of the parameter that you want AWS WAF to search, for example, UserName or SalesRegion . The parameter name is not case sensitive.
If the value of Type is any other value, omit Data .


TextTransformation -> (string)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on FieldToMatch before inspecting it for a match.
You can only specify a single type of TextTransformation.
Note that if you choose BODY for the value of Type , you must choose NONE for TextTransformation because CloudFront forwards only the first 8192 bytes for inspection.

NONE

Specify NONE if you donât want to perform any text transformations.

CMD_LINE

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

Delete the following characters: â â ^
Delete spaces before the following characters: / (
Replace the following characters with a space: , ;
Replace multiple spaces with one space
Convert uppercase letters (A-Z) to lowercase (a-z)


COMPRESS_WHITE_SPACE

Use this option to replace the following characters with a space character (decimal 32):

f, formfeed, decimal 12
t, tab, decimal 9
n, newline, decimal 10
r, carriage return, decimal 13
v, vertical tab, decimal 11
non-breaking space, decimal 160


COMPRESS_WHITE_SPACE also replaces multiple spaces with one space.
HTML_ENTITY_DECODE

Use this option to replace HTML-encoded characters with unencoded characters. HTML_ENTITY_DECODE performs the following operations:

Replaces (ampersand)quot; with "
Replaces (ampersand)nbsp; with a non-breaking space, decimal 160
Replaces (ampersand)lt; with a âless thanâ symbol
Replaces (ampersand)gt; with >
Replaces characters that are represented in hexadecimal format, (ampersand)#xhhhh; , with the corresponding characters
Replaces characters that are represented in decimal format, (ampersand)#nnnn; , with the corresponding characters


LOWERCASE

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

URL_DECODE

Use this option to decode a URL-encoded value.

ComparisonOperator -> (string)

The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided Size and FieldToMatch to build an expression in the form of âSize ComparisonOperator size in bytes of FieldToMatch â. If that expression is true, the SizeConstraint is considered to match.

EQ : Used to test if the Size is equal to the size of the FieldToMatch
NE : Used to test if the Size is not equal to the size of the FieldToMatch
LE : Used to test if the Size is less than or equal to the size of the FieldToMatch
LT : Used to test if the Size is strictly less than the size of the FieldToMatch
GE : Used to test if the Size is greater than or equal to the size of the FieldToMatch
GT : Used to test if the Size is strictly greater than the size of the FieldToMatch


Size -> (long)

The size in bytes that you want AWS WAF to compare against the size of the specified FieldToMatch . AWS WAF uses this in combination with ComparisonOperator and FieldToMatch to build an expression in the form of âSize ComparisonOperator size in bytes of FieldToMatch â. If that expression is true, the SizeConstraint is considered to match.
Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).
If you specify URI for the value of Type , the / in the URI counts as one character. For example, the URI /logo.jpg is nine characters long.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf-regional", "update-size-constraint-set", "size-constraint-set-id", "change-token", "updates", add_option_dict)
