# Postmortem

![](https://media.giphy.com/media/zOvBKUUEERdNm/giphy.gif)

## Issue Summary
---
Apache is returning a 500 error, this trouble makes that 100% of people tryng ot retrieve information for server wasn't possible to make some request.

**SPAN** 15:00 - 19:30 COT


# Timeline
---
* 15:00 COT - Problem was discovered
* 16:00 COT - Fellow engineers attempt to resolve issues through various means
* 17:15 COT - Issue was brought to the attention of the engineer on call while trying to bring some response from server
* 17:45 COT - Discovered that it is imperative to debug each process at server status
* 18:00 COT - Discovered that child process from apache is not finishing well
* 18:15 COT - Attach each running process from child ṕrocess at apache runtime
* 18:30 COT - Discovered unresolved references from routes of some files
* 19:30 COT - Problem was resolved

## Root Cause
---
While trying to resolve the issue using several methods of debugging found that a path were not found with extension of .phpp
and this files its located with .php extension.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/P61xMkZ/issue.png" alt="issue" border="0"></a>


## Corrective and preventative measures
---
* Before locating paths in any file , watch carefully extensions for any file
* At any moment for changing config files, do not wait for another to run server status, the one in charge for deploy must check this out
* Do not manually change paths, try to automate it with bash scripts in order to prevent this issues

