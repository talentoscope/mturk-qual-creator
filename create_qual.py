import boto
from boto.mturk.connection import MTurkConnection

# Create the connection to MTurk
mtc = MTurkConnection(aws_access_key_id='MYACCESSKEYID',
aws_secret_access_key='MYSECRETACCESSKEY',
host='mechanicalturk.amazonaws.com')

# Print account balance to show connection is working
account_balance = mtc.get_account_balance()[0]
print "You have a balance of: {}".format(account_balance)

# Create the qualification
response = mtc.create_qualification_type(name="NAME", description="DESCRIPTION", status="Active|Inactive", auto_granted=True|False, auto_granted_value=###)
