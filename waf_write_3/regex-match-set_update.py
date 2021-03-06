#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-regex-match-set.html
if __name__ == '__main__':
    """
	create-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-match-set.html
	delete-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-regex-match-set.html
	get-regex-match-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-regex-match-set.html
	list-regex-match-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-regex-match-sets.html
    """

    parameter_display_string = """
    # regex-match-set-id : The RegexMatchSetId of the  RegexMatchSet that you want to update. RegexMatchSetId is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .
    # updates : An array of RegexMatchSetUpdate objects that you want to insert into or delete from a  RegexMatchSet . For more information, see  RegexMatchTuple .
(structure)


Note
This is AWS WAF Classic documentation. For more information, see AWS WAF Classic in the developer guide.

For the latest version of AWS WAF , use the AWS WAFV2 API and see the AWS WAF Developer Guide . With the latest version, AWS WAF has a single set of endpoints for regional and global use.


In an  UpdateRegexMatchSet request, RegexMatchSetUpdate specifies whether to insert or delete a  RegexMatchTuple and includes the settings for the RegexMatchTuple .
Action -> (string)

Specifies whether to insert or delete a  RegexMatchTuple .

RegexMatchTuple -> (structure)

Information about the part of a web request that you want AWS WAF to inspect and the identifier of the regular expression (regex) pattern that you want AWS WAF to search for. If you specify DELETE for the value of Action , the RegexMatchTuple values must exactly match the values in the RegexMatchTuple that you want to delete from the RegexMatchSet .
FieldToMatch -> (structure)

Specifies where in a web request to look for the RegexPatternSet .
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

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on RegexPatternSet before inspecting a request for a match.
You can only specify a single type of TextTransformation.

CMD_LINE

When youâre concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

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

NONE

Specify NONE if you donât want to perform any text transformations.

RegexPatternSetId -> (string)

The RegexPatternSetId for a RegexPatternSet . You use RegexPatternSetId to get information about a RegexPatternSet (see  GetRegexPatternSet ), update a RegexPatternSet (see  UpdateRegexPatternSet ), insert a RegexPatternSet into a RegexMatchSet or delete one from a RegexMatchSet (see  UpdateRegexMatchSet ), and delete an RegexPatternSet from AWS WAF (see  DeleteRegexPatternSet ).

RegexPatternSetId is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .
    # change-token : The value returned by the most recent call to  GetChangeToken .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "update-regex-match-set", "regex-match-set-id", "updates", "change-token", add_option_dict)
