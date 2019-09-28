Title: MITRE on Threat Detection
Date: 2019-04-25 17:37
Author: jinhaochan
Category: Security
Tags: MITRE
Slug: mitre-on-threat-detection
Status: published



I just sat through a webinar by the folks at Red Canary, and they covered some questions regarding threat detection using the MITRE ATT&CK framework.





The webinar sat down with the researchers who created MITRE, and it was quite insightful. Here are some of the notes I took that may be useful for present and future work:



<!-- wp:heading {"level":3} -->

### Top 10 MITRE ATT&CK Techniques





------------------------------------------------------------------------




<!-- wp:list {"ordered":true} -->

1.  Powershell
2.  Scripting
3.  Regsvr32
4.  Connection proxy
5.  Spearphising
6.  Masquerading
7.  Credential Dumping
8.  Registry run keys
9.  Rundll32
10. Service Execution





We can observe that a bulk of the these techniques are actually native operating system utilities, and that adversaries are leveraging on these preinstalled utilities to carry out their attacks. Things like Powershell, Regsvr32 and Rundll32 are very common things that are executed in benign settings.





The implications of this is that we simply can't just "turn off" these services in an attempt to disrupt their Cyber Kill Chain. What has to be done is proper logging and auditing of these services.





For example, we need to turn on logging for Powershell command line, or cmd.exe command line parameters to observe what command is being ran. Also, we need to turn on process tracking to identify which process spawns what other processes. If Microsoft Word spawns cmd.exe or Powershell, we know that something is highly suspicious.





That being said, there needs to be a fine balance to ensure we don't get too much log by enabling everything. Most activities are normally benign, and having too much logging will induced noise, which may invariably hide the malicious activities!



<!-- wp:heading {"level":3} -->

### Top Data Sources for leveraging on MITRE ATT&CK  





------------------------------------------------------------------------




<!-- wp:list {"ordered":true} -->

1.  Process Monitoring
2.  File Monitoring
3.  Process Command-line Parameters
4.  API monitoring
5.  Process use of network
6.  Windows Registry
7.  Packet capture
8.  Authentication Logs
9.  Netflow
10. Windows Event Logs
11. Network Protocol Analysis
12. Binary file metadata
13. DLL monitoring
14. Loaded DLL
15. System Calls





If that list is too much, or you find that it's too noisy (or your sysadmin policy says you can't enable such logging), then there is a bare minimum data source is required for threat hunting:



<!-- wp:list {"ordered":true} -->

1.  Windows Registry
2.  File Monitoring
3.  Process Command-line Parameters
4.  Process Monitoring





These 4 telemetry provides a comprehensive enough picture to perform threat hunting. These 4 data sources will cover most crucial end-point activities. There isn't any network components in this, but that can be incorporated if needed.



<!-- wp:heading {"level":3} -->

### **How do you build up threat hunting plan based on MITRE ATT&CK?**





------------------------------------------------------------------------






**Know the questions you want to answer, and construct hypotheses around them. Evaluate these hypothesis using various data sources.**





Don't in go blindly. Threat hunting has to be done in a directed manner, and you need to know what you're hunting.



<!-- wp:heading {"level":3} -->

### Tools to assist in Threat Hunting





------------------------------------------------------------------------






-   DetectionLab by Chris Long
-   ThreatHuting splunk app by Olaf Hartong
-   PoSh\_ATTCK by ENRW
-   ATT&CK Navigator
-   Atomic Red Team





I've not used the DetectionLab, but I've used the rest quite extensively.





The data resource by Olaf Hartong is really comprehensive, as it covers most TTPs. However, most of the queries are Sysmon oriented, so if your environment does not support Sysmon, you have to find way to tweak the Sysmon queries to match your environment.





PoSh\_ATTCK seems to be a Powershell replica of MITRE, and I did not really find much value add in it.





ATT&CK Navigator is the standard way of browsing the TTPs. Standard, but very useful. They even link the TTPs to suspected APT groups, which can assist in attribution.





Atomic Red Team is a really useful resource in providing atomic tests to execute. This allows you to replay attacks, and get first hand data in your environment. However, it does not cover all the attacks, and there are some TTPs that are still missing in their atomic test list. Still, a very good resource.  


