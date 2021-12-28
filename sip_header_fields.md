# Information about SIP  header fields


```
SIP = {"METHOD": ['INVITE', 'PRACK', 'ACK', 'SUBSCRIBE', 'NOTIFY', 'SIP/2.0 200 OK', 'BYE', 'OPTIONS', 'REFER'],
       "REMOTE_CALLEE": REMOTE_EXT,   #who receives a telephone call
       "REMOTE_PBX_IP": REMOTE_PBX_IP,
       "LOCAL_PBX_IP": LOCAL_PBX_IP,
       "LOCAL_PBX_CALLER": LOCAL_PBX_EXT, #who initiate a telephone call
       "USER": USER,
       "TRANSPORT": TRANSPORT,
       "REMOTE_PBX_GROUP": REMOTE_PBX_GROUP,
       "REMOTE_PBX_CONTEXT": REMOTE_CONTEXT,
       "REMOTE_PBX_TAG": REMOTE_TAG,
       "REMOTE_PBX_MSG": REMOTE_MSG,
       "REMOTE_PBX_PURPOSE": REMOTE_PURPOSE,
       "LOCAL_PBX_GROUP": REMOTE_TGROUP,
       "LOCAL_PBX_CONTEXT": REMOTE_CONTEXT,
       "LOCAL_PBX_BRANCH": 'BRANCH_ID',
       "RINSTANCE": 'REINSTANCE_NO',
       "LOCAL_PBX_TAG": 'REMOTE_TAG',
       "LOCAL_PBX_CALL_ID": 'REMOTE_CALL_ID',
       "CSEQ_NO": 'CSEQ_NO',
       "CSEQ_NOTIFY": 'NOTIFYNO',
       "RACK": 'RACK METHOD',
       "CSEQ_METHOD": ['INVITE', 'PRACK', 'ACK', 'SUBSCRIBE', 'NOTIFY', 'SIP/2.0 200 OK', 'BYE', 'OPTIONS', 'REFER'],
       "S-EXPIRES": '7200;refresher=uas',
                    "MIN_SE": '90',
                    "ALERT-INFO_A": '<urn:alert:source:internal>',
                    "ALERT-INFO_B": '<urn:alert:service:normal>',
                    "ALLOW": 'INVITE, OPTIONS, BYE, ACK, CANCEL, INFO, REGISTER, REFER,PRACK, SUBSCRIBE, NOTIFY, MESSAGE, UPDATE, PUBLISH',
                    "CONTENT_TYPE": 'application/call-completion',
                    "SUPPORTED": ['timer', 'replaces', '100rel'],
                    "USER_AGENT": 'LOCAL_PBX SN/17.3.1.1.14',
                    "PRIVACY": 'none;private_none',
                    "PA_IDENTITY": '<sip:{}@{};tgrp={};trunk-context={}>'.format(LOCAL_PBX_CALLER, LOCAL_PBX_IP, LOCAL_PBX_GROU, LOCAL_PBX_CONTEXT),
                    "CONTENT_LENGHT": CONTENT_LENGHT,
                    "EVENT": 'call-completion',
                    "M": ['BS', 'NR', 'NL'],
                    "SUBSCRIPTION_STATE": '{};{}'.format('terminated', 'reason=timeout'),
       }
```
