Title: The Cyber Kill Chain
Date: 2019-05-13 16:52
Author: Chan Jin Hao
Category: Security
Tags: Cyber kill chain
Slug: the-cyber-kill-chain
Status: published



The Cyber Kill Chain (CKC) is a sequential set of steps that takes place when an attack happens. There are many variations of the CKC by different companies such as , but the "trusted" and most convincing variant is by Lockheed Martin.



<!-- wp:image {"id":447} -->


![placeholder]({attach}media/2019/05/the-cyber-kill-chain-body.png.pc-adaptive.1920.medium.png){.wp-image-447}






This CKC is pretty straightforward, and by disrupting any part of the kill chain, you can stop the final attack, which is "Actions On Objectives"





At each step, there are examples of what an Adversary could do, and what Defenders can do to detect or disrupt it.



<!-- wp:heading {"level":3} -->

### Reconnaissance





------------------------------------------------------------------------






Before carrying out the attack, the adversary will scope out and survey the target. This phase is extremely broad, and can cover technical and non-technical aspects.





For example, they can find out the working hours of your system administrator to plan the right time to attack, or find out what version of OS and email application the company is using. They can harvest emails or contact information through OSINT channels, or social media. They can find scan for open services in the company network.





Because of such a broad scope of activities, it's almost impossible to be aware that someone is performing reconnaissance on your company. What you can do however lies on the technical side, such as:





-   Enabling logging for your webservers to detect any sort of scraping or probing.
-   Disabling all unneeded services
-   Disabling ICMP responses
-   Properly configuring your Firewall to log and prevent network traffic





**Detection**:





-





**Prevention**:





The goal here is to prevent information leakage, as well as detecting information probing attempts. Knowing that an attack is going to happen is the first step to protecting yourself.



<!-- wp:heading {"level":3} -->

### Weaponization





------------------------------------------------------------------------






In this stage, the adversary starts to prepare the payload for attack.





Given the information he got from reconnaissance, he can build tools specific for OS versions, application versions or Firewall versions. Since this phase of the attack happens outside the victims circle of control, there is no way of detecting when Weaponization happens.





**Detection:**





-





**Prevention:**





One possible way of neutralizing this phase is to do regular security assessments of your infrastructure, and detect if any applications or versions are vulnerable, and perform patching to secure those assets.





By doing so, you are preventing, or making it very hard for adversaries to perform Weaponization.



<!-- wp:heading {"level":3} -->

### Delivery





------------------------------------------------------------------------






In the delivery stage, the attacker sends the Weaponized tools to the victim, either via software (Email, links, direct to the webserver) or physical means (USB insertion)





This is the most crucial stage for defenders. Knowing what are all the possible vectors of attacks, and either mitigating it, or eliminating it if possible.





You must know which are your most important infrastructures that are connected to the most important assets, and make sure that they are well secured with various layers of security.





**Detection:**





Logging must also be enabled to detect any point of entry, such as email logs, web logs and endpoint logs.





**Prevention:**





Airgapped machines, web proxies and proper staff security education all limit the vectors of delivery.



<!-- wp:heading {"level":3} -->

### Exploitation





------------------------------------------------------------------------






If you failed to prevent Delivery, the adversaries would be able to enter the machine. Once inside, the next step for them is to perform exploitation to either gain privilege escalation, or to gain unauthorized information. This can either be a software or hardware vulnerability that the adversary leverages on.





Preventing exploitation is a huge monster of a topic on it's own, but basically it revolves around patching your systems, making sure appropriate security controls are in place, and properly educating your staff on security issues like phishing emails and malicious links.





Also, regular security assessments should be done to lock down all possible edge cases.





**Detection:**





Endpoint security and application logging





**Prevention:**





By hardening your systems and educating your users, you're limiting the amount of damage that can be done if the adversary is within your network.



<!-- wp:heading {"level":3} -->

### Installation





------------------------------------------------------------------------






Once the adversary gets into your system and performs exploitation, it is highly likely that he would have escalated privileges, and can install other tools he wants to allow him to perform other actions.





These tools includes keyloggers, rootkits, backdoors, webshells or scripts.





**Detection:**





Detection at this phase involves behavioral analysis. HIPS, endpoint detection tools, and log analysis can be used to detect anomalous activities on both the endpoint and network.





**Prevention:**





At this phase, since the adversary already has exploited the system and has escalated privilege. There is little you can do to prevention, but only detection and performing remediation.



<!-- wp:heading {"level":3} -->

### Command & Control





------------------------------------------------------------------------






After installing rootkits and backdoors, the malware needs to receive commands remotely from their server. This is done by establishing a C2 connection out from the victim machine to the adversary.





C2 communication is hard to detect, and it can take place under commonly used ports and services such as HTTP, DNS or SMTP.





**Detection:**





Network based detection can be used to find anomalous activities on the network. Web proxies to log all traffic for analysis.





**Prevention:**





Blocking and preventing unauthorized network traffic. Disabling unneeded services that connect out to the internet. Close unused ports. Honey pots to study the C2 traffic.



<!-- wp:heading {"level":3} -->

### Actions On Objectives





------------------------------------------------------------------------






In the CKC, it shows this as the final step after performing all previous actions. Actions On Objects could mean acquiring user credentials, collecting and exfiltrating data or lateral movement. But these actions need not be the final step of the CKC, after establishing a C2 or performing Exploitation.





Depending on the objective the adversary wants to perform, Actions On Objectives could actually happen after the Exploitation phase onward.





This phase is an accumulation of steps, thus there is no single point of detection or prevention. To disrupt this part of the kill chain, you have to target all preceding parts of the CKC.





**Detection:**





Logging on network and endpoint to perform anomaly detection.





**Prevention:**





Preventing Delivery and Exploitation would prevent the adversaries to perform any Actions, thus preventing this final step of the CKC.





Installation cannot be prevented, since it assumes that the adversary has escalated privileges, and a C2 connection may not be required to perform an Action On Objectives.


