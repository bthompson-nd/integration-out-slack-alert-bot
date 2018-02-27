#!/home/bthomps5/outmon/bin/python

from config import *
import requests, json
from simple_salesforce import Salesforce

sf = Salesforce(username=USERNAME, password=PASSWORD, security_token=SECURITY_TOKEN, sandbox=SANDBOX, organizationId=ORGANIZATION_ID)
data = sf.query_all("select count() from integration_out__c where status__c in ('',null)")

if data['totalSize'] > ROW_THRESHOLD:
    requests.post(REST_ENDPOINT, data=json.dumps({'text': ALERT_TEXT.format(data['totalSize'])}))
