Title: Accelerate
Date: 2020-06-10 21:32
Author: Chan Jin Hao
Category: Review
Slug: hit-refresh
Status: published


A book not only about DevOps, but about the surrounding culture to enable it

[Click here for the book](https://www.amazon.sg/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339)


This book breaks things down nicely into the actionable segments that you can take to enable a fast and dynamic organization. It talks about DevOps, but you'll come to realize that it's not all about DevOps, and theres so many other modes of agile thinking and leadership that is required for all of it to work.

## Measuring Performance
---

We should be thinking in terms of capabilities, and not "Maturity". A maturity of a company tells us nothing about what it can do, while capabilities tells us how efficient and capable the company is. Thinking in terms of capabilities means that we need ask questions about our processes, what we can do, and how efficiently we can do it. To quantify those questions into measurable metrics, we use 4 indicators

1. Lead Time
2. Deployment Frequency
3. Time to Restore
4. Change Fail Rate

When we talk about lead time, there are 2 parts to it: Design Lead Time and Delivery Lead Time. Design Lead Time something that is hard to measure, and it's mostly subjective. How and when are the designers happy with the features, look, and architecture of a product? That is something hard to quantify. Delivery Lead Time however, is from the time any new code is committed, to the time it appears and is usable in production. The time difference between commit and delivery is the Delivery Lead Time, and what happens in between is ideally automated activities such as unit/integration/systems testing.

Deployment Frequency is simply how frequent code is being pushed out. Delivery Lead Time, together with Deployment Frequency, tells you the Tempo of a company. Time to Restore is the time to recover failed services, and Change Fail Rate is the rate of errors for each deployment.

High functioning companies:

- Lead Time: Less than 1 hour
- Deployment Frequency: Multiple times a day
- Time to Restore: Less than 1 hour
- Change Fail Rate: 0% - 15%

Low functioning companies:

- Lead Time: One week - One month
- Deployment Frequency Once a week - Once a month
- Time to Restore: One day - One week
- Change Fail Rate: 31% - 45%

We can see that high performing companies move extremely fast, with all 3 time metrics falling within a single day. To achieve those crazy levels of efficiency, it needs to be enabled the following

## 1. CI/CD

This is where the concepts of DevOps comes in. Putting them in bullet points:

- Work in small batches, and commit often to master
- From frequent pushes to master, automate the deployment of new code to production
- Testing should not be outsourced, but created by the very developers of the program. Testing should also be automated
- Have proper test data. Upfront time is need to curate and make this test data comphrensive. Dont skimp on it.
- Have a proper configuration management for each environment. Define your configs for dev, staging and production
- Version Control (need not say more about this)

## 2. Architecture

Obviously put, the architecture should be loose. The buzzword these days are "microservices", which works. This gives your product two important characteristics: Deployability, and Testability. These two features synergizes well with the points above about CI/CD. By lowering the barrier to deploying to production, and making testing much simpler.

On a cultural point, when building the architecture, allow your developers to choose their own tools. They should be busy thinking about the outcomes, and not bickering about what tools to use.

## 3. Lean Management

- Limit Work In Progress (WIP). This means not piling a bunch of work onto a developer all at once, forcing him/her to perform costly context switching
- Visual Displays of metrics, such as bugs, to-do features and backlogs
- Obtain Feedback fast and often, and seriously implement them in the design. The customer is king
- Lightweight Change Management process. Your develop will go crazy if he has to jump through 3 hoops just to make a single line of change
- Use Peer Review to analyze and stamp your codes, such as pair programming, or intrateam code review.

## 4. Product Development

When it comes to the actual development of the product:

- Work in small batches (as mentioned above in CI/CD)
- Make sure everyone understands the workflow
- Seek and use feedback (enabled by lean management)
- Allow team experimentation, and empower the developers some degree of authority to explore technologies

## 5. Making Work Sustainable

The number fear and anxiety developers have is the process of deployment to production. This sits at the 3rd and 4th point of Time to Restore and Change Fail Rate.

The solution is mentioned a few times in the points above, and it has to do largely with automation and proper management. With a combination of CI/CD practices and Lean Management, it allows the team to navigate this space more confidently, thus reducing their anxiety levels.

## 6. Proper Leadership

They draw a distinction here between Servant Leadership (focus on development and performance of the staff) vs Transformational Leadership (Inspiring staff to identify with the organization and it's mission). Having both types of leaders is a must.

A Transformational Leader must have and provide:

- Vision
- Inspirational Communication
- Intellectual Stimuation
- Supportive Leadership
- Personal Recognition

!! Hack and Yak days !! Days to create (hack) and days to clear technical debt (yak)

Most importantly, the leaders must provide a culture of learning and cross-functional collaboration.


## Conclusion

Those were the key pointers in the book, and a large section of it was dedicated to the scientific methods used to back the study up. I really liked that portion, as it shows that these qualities defined above are "scientific", and not just pulled out of the air.

That's not to say that by following steps 1-7, your company will find incredible success. It would transform and accelerate your technical capabilities by a huge amount, but thats only one side of the business. Technology afterall, is an enabler, and as to what it enables and how you use this process, that determines your success.
