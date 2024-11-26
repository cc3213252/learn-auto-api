pip install -r api/requirements.txt

## 测试步骤

python infra_api.py  
curl localhost:8000/location  

```bash
(pulumi) cyd:learn-auto-api cyd$ python infra_api.py 
Serving on port 8000...
info: Initializing stack...
info: Successfully initialized stack
info: Setting project config...
info: Successfully set project config
info: Refreshing stack...
Refreshing (dev)

View Live: https://app.pulumi.com/cc3213252/api/dev/updates/1


Resources:

Duration: 1s

info: Successfully refreshed stack
info: Updating stack...
Updating (dev)

View Live: https://app.pulumi.com/cc3213252/api/dev/updates/2


@ Updating....
 +  pulumi:pulumi:Stack api-dev creating (0s)
@ Updating.........
 +  aws:iam:Role role-2 creating (0s)
@ Updating.....
 +  aws:iam:Role role-2 created (1s)
 +  aws:iam:RolePolicyAttachment role-policy creating (0s)
 +  aws:lambda:Function location-finder creating (0s)
@ Updating....
 +  aws:iam:RolePolicyAttachment role-policy created (0.83s)
@ Updating...............
 +  aws:lambda:Function location-finder created (12s)
@ Updating.....
 +  aws:lambda:Invocation test-invoke creating (0s)
@ Updating....
+  aws:lambda:Invocation test-invoke created (0.76s)
 +  pulumi:pulumi:Stack api-dev created (24s)
Outputs:
    location: "\"us-east-1\""

Resources:
    + 5 created

Duration: 26s

info: Successfully updated stack
info: Summary: 
{
    "create": 5
}
info: Output: "us-east-1"
info: Destroying stack...
Destroying (dev)

View Live: https://app.pulumi.com/cc3213252/api/dev/updates/3


@ Destroying....
 -  aws:lambda:Invocation test-invoke deleting (0s)
@ Destroying.....
 -  aws:lambda:Invocation test-invoke deleted (2s)
 -  aws:iam:RolePolicyAttachment role-policy deleting (0s)
 -  aws:lambda:Function location-finder deleting (0s)
@ Destroying.....
 -  aws:lambda:Function location-finder deleted (1s)
@ Destroying................................
 -  aws:iam:RolePolicyAttachment role-policy deleted (31s)
@ Destroying....
 -  aws:iam:Role role-2 deleting (0s)
@ Destroying....
 -  aws:iam:Role role-2 deleted (0.93s)
 -  pulumi:pulumi:Stack api-dev deleting (0s)
@ Destroying....
 -  pulumi:pulumi:Stack api-dev deleted (0.31s)
Outputs:
  - location: "\"us-east-1\""

Resources:
    - 5 deleted

Duration: 38s
The resources in the stack have been deleted, but the history and configuration associated with the stack are still maintained.
If you want to remove the stack completely, run `pulumi stack rm dev`.
info: Successfully destroyed stack
127.0.0.1 - - [26/Nov/2024 19:45:18] "GET /location HTTP/1.1" 200 45

```