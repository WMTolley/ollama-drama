[CS5704] Software Engineering

Dr. Chris Brown
Virginia Tech
1/22/2026

SE Processes

SE History
Plan-Driven and Iterative Process Models
Agile Development and Project Management
AI + SE Processes
Version Control

Learning Outcomes

By the end of the course, students should be able to:
Implement a software system following the software life cycle phases
Develop software engineering skills working on a team project
Identify processes related to phases of the software lifecycle
Explain the differences between software engineering processes
Discuss research questions and studies related to software engineering
Communicate (via demo and writing) details about a developed software application

‹#›

Announcements

HW0 due Friday (1/30) before midnight
Syllabus Survey
Mattermost Introduction
Software Configuration
The workshop activity next class will rely on the Docker installation!
Brainstorm Project 1 ideas/groups

‹#›

Warm-Up

Discuss: What is your experience with software engineering processes?

‹#›

What is SE?

A discipline that encompasses:
the process of software development
methods for software analysis, design, construction, testing, and maintenance
tools that support the process and the methods
[Pressman]

‹#›



Processes, Methods, and Tools

Various tasks are required to build and maintain software
• SE process: the organization and management of these tasks
• SE methods: ways to perform the tasks
• SE tools: assist in perform the tasks

‹#›

SE History

Why study software engineering history?
To learn what has been done before and how we got here.
CS/SE is not that old, compared to other disciplines.
Don’t remember failures? Likely to repeat them
Don’t remember successes? Unlikely to repeat them
“Those who cannot remember the past are condemned to repeat it.” – Santayana [https://liberalarts.vt.edu/magazine/2017/history-repeating.html]

‹#›

History of Computer Programming

1843: Sequence of steps from Ada Lovelace to Charles Babbage considered first computer program
1889: Hollerith tabulating machine

‹#›

1940s: First electronic computers
1956: First programming language - FORTRAN

History of Software Engineering

1950s: Engineer software like hardware

‹#›

First programming languages
1956: FORTRAN (Formula Translation);
1958: LISP (List Processor);
1959: COBOL (Common Business Oriented Language);
Punch cards
No formal SE processes
Code-and-fix

Code-and-Fix

Based on a given a project specification:
Write code
Improve it
GOTO 1

‹#›

When should you use Code-and-Fix?
Maybe small 1-person projects and/or course assignments
Never 🛑
Lacks requirements, systematic testing, maintainability,...

History of SE (cont.)

1960s: Software is NOT like hardware

‹#›

Different properties:
invisible, complex, difficult to change, unconstrained by physical laws of nature,…
Demand for programmers exceeded supply
First college Computer Science departments formed 🎓
1962: Purdue University
First use of the term “software engineering”!

“Software Engineering”

‹#›

1963/1964: “While developing the guidance and navigations systems for the Apollo missions, computer scientist and systems engineer Margaret Hamilton coins the term ‘software engineering’. Hamilton felt that software developers earned the right to be called engineers.” [Juhasz]

History of SE (cont.)

1960s (cont.): Software is NOT like hardware

‹#›

Still disorganized, but with better infrastructure
Operating systems, compilers, utilities, etc.
Some successes:
Apollo
Electronic switching systems (ESS)
Problems:
– Unmaintainable spaghetti code
– Unreliable, undiagnosable systems
– Software development is too expensive

History of SE (cont.)

1970s: Software costs surpass hardware

‹#›

Structural SE processes begin to form!

What is a SE process?

– a framework for the tasks that are required to build high-quality software to provide stability, control and organization to an otherwise chaotic activity [Pressman]
– a software development process defines who does what, when, in order to build a piece of software. [Wilson]

‹#›

Elements of SE Processes

‹#›

History of SE (cont.)

1970s: Software costs surpass hardware

‹#›

Structural programming processes
Formal approaches begin to form
Specification
Development
Verification
Punch cards starting to become obsolete…
Plan-Driven process models

Plan-Driven Models

Also known as incremental development
The process is divided into small, workable increments. Each succeeding increment builds on the work completed in the previous increment.

‹#›

Waterfall Model

The “classic” SE process model

‹#›

Waterfall Assumptions

• All requirements are known at the start and stable
• Risks (unknowns) can be turned into knowns through schedule-based invention and innovation
• The design can be done abstractly and speculatively.
• Everything will work when we start integration.

‹#›

Waterfall Pros and Cons

Pros:
– Widely used and systematic
– Good for projects with well-defined requirements
– Development cost minimized by up front planning
– Fits needs for managers, accountants, lawyers, etc. (i.e. not developers)

Cons:
– Assumes all requirements are known at the start
– Cannot predict risk and design
– Working programs are not available early
– Assumes everything will fit together during integration
– Expensive and time-consuming

‹#›

V-Model

Extension of the waterfall model
Greater emphasis on design and testing!

‹#›

When to use plan-driven models?

Working for big clients that enforce formal approaches (i.e. government)
Working on fixed-scope, fixed-price contracts without many rapid changes
For safety- and mission-critical systems
Work in an experienced team

‹#›

Success Story: Space Shuttle

As the 120-ton space shuttle sits surrounded by almost
4 million pounds of rocket fuel, exhaling noxious fumes, visibly impatient to defy
gravity, its on-board computers take command.
Charles Fishman, 1996

‹#›

Success Story (cont.)

“This software is bug-free”
• Some impressive statistics
– The last 3 versions of the program--420,000 lines of code had just 1 error each
– The last 11 versions of the code had 17 errors total
– Commercial programs of equivalent complexity today would have over 5,000 errors

‹#›

How did they get it right?

• 1/3 of the process before coding
• NASA and Lockheed Martin groups agree in the most minute detail about everything
• Specs are almost pseudo-code
• Nothing in the specs is changed without agreement and understanding
Ex.) Task to upgrade software to add GPS navigation
– 1.5% changes in program/6366 LOC
– 2500 page specs for the change

‹#›

But, how much did it cost?

• 260 people
• >40,000 pages of specifications
• 20 years
• $35 million Annual budget
• $700 million overall budget
• 700 million/420k = $1600/line of code

‹#›

History of SE (cont.)

1980s: More Productivity, Less Plan-Driven

‹#›

Major productivity enhancements
– Working faster: tools and environments
– Working smarter: processes and methods
– Work avoidance: code reuse, simplicity, objects
Iterative process models
Other trends: Code reuse libraries, codes of ethics, licenses, Object oriented…
Smalltalk, Eiffel, Ada, C++

History of SE (cont.)

1990s: More Iterative

‹#›



Growing divide between plan-driven and iterative models
Standish Group CHAOS Report
Other trends: Open source software, reverse engineering, computer viruses, etc.
Modern programming languages
Java, Python, JavaScript, Ruby, etc.
End-user programming: HTML, CSS, R, etc.

Data by the Standish Group (1995)

• $81B on canceled projects, $59B budget overruns
Only 1/6 projects were completed on time and within budget
Nearly 1/3 projects were canceled
Over half projects were considered “challenged”
• Among canceled and challenged projects
– Budget overrun: 189% of original estimate
– Time overrun: 222% of original estimate
– Only 61% of the originally specified features

‹#›

The CHAOS Report 1995

‹#›

[Standish Group]

“In the United States, we spend more than $250 billion each year on IT application development…A great many of these projects will fail. Software development projects are in chaos, and we can no longer imitate the three monkeys -- hear no failures, see no failures, speak no failures. The Standish Group research shows a staggering 31.1% of projects will be canceled before they ever get completed. Further results indicate 52.7% of projects will cost 189% of their original estimates. The cost of these failures and overruns are just the tip of the proverbial iceberg.”

The CHAOS Report 1995

Top 3 reasons for project failure:

[Standish group 1995]

Top 3 reasons for project success:

‹#›

Iterative Models (cont.)

Modern software process models
Software is developed through repeated cycles (iterations).
Easier to modify code, design, etc.
Faster operational product (weeks vs months)
Usually more user involvement

‹#›

Iterations

Iterations should be short (2-6 weeks)
Small steps, rapid feedback and adaptation
Massive teams with lots of communication
Iterations should be time-boxed (fixed length)
Integrate, test and deliver the system by a scheduled date
If not possible: move tasks to the next iteration
Improves programmer productivity with deadlines
Encourages prioritization and decisiveness

‹#›

Incremental Model

An iterative sequence of waterfall models

‹#›

Prototyping Model



‹#›



Spiral Model



‹#›

Spiral Model

A risk-driven evolutionary model
What is risk?
Anything that can go wrong! Ex.) bugs, new features, budget, changing requirements, new technologies, team member absences/departures, deadlines,...

‹#›

Spiral Phases

Objective setting
– Define specific objectives, constraints, products, plans
– Identify risks and alternative strategies
Risk assessment and reduction
– Analyze risks and take steps to reduce risks
Development and validation
– Pick development methods based on risks
Planning
– Review project and decide whether to continue with another loop

‹#›

1

2

4

3

Risk Management (Sommerville)



‹#›

Incremental vs Prototyping vs Spiral

All are iterative models 🔁
Incremental: Release-driven
Get product out to users quickly!
Prototyping: Client-driven
Get feedback from users/clients!
Spiral: Risk-driven
Prevent and minimize risk!

‹#›

History of SE (cont.)

2000s-present: Process Synthesis

‹#›

2001: Agile manifesto
2004: Software Engineering Body of Knowledge (SWEBOK)
Model, feature, and test-driven development
Service-oriented software
Hybrid agile/plan-driven processes
…

Roots of Agile

Direct response to waterfall and plan-driven processes
Requirements will change
Initial design will be inaccurate
Implementation will need to be flexible
Risks are inevitable
Desire for more lightweight approaches with less planning and process artifacts.

‹#›

Roots of Agile (cont.)

Remember: plan-driven methods work great for government, lawyers, managers, etc.
Agile focuses on developers: the talents and skills of individuals, needs of the team.

‹#›

“Agile development practices are almost as old as programming, but they came into their own with the rise of the web in the late 1990s.” [Wilson]

The Agile Manifesto

We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:
Individuals and interactions over processes and tools
Working software over comprehensive documentation
Customer collaboration over contract negotiation
Responding to change over following a plan
- That is, while there is value in the items on the right, we value the items on the left more.
[Kent Beck et al, 2001]

‹#›



What is Agile?

Time-boxed, iterative, and evolutionary development framework that promotes:
– adaptive planning
– evolutionary development
– incremental delivery
– rapid and flexible response to change
Any iterative process can be applied with an agile spirit!

‹#›

Key Points of Agile Planning

“Agile methods derive much of their agility relying on tacit knowledge embodied in the team, rather than writing the knowledge down in plans.” [Boehm]

‹#›

Agile Planning and Modeling

The purpose is to understand, not to document.
Diagrams/models are typically thrown away, if used at all.
Keep it simple
Avoid unnecessary artifacts
Only high-level plans/models
Plans are inaccurate
Only tested code demonstrates true design!

‹#›

Agile Development

Agile is not a software engineering process model, but has led to the creation of several models…
Extreme Programming
Adaptive Software Development…
In addition to contributing other development strategies and frameworks.
Kanban & Scrum
Lean Software Development
Crystal Agile Framework
DevOps (later this semester)...

‹#›

Extreme Programming (XP)

[Pressman]

‹#›

Adaptive Software Development (ASD)

[Pressman]

‹#›

\* More focus on human collaboration, team organization.

Kanban and Scrum

Two different strategies for implementing agile development practices
Can be combined with other processes, strategies, etc. (i.e. Scrumban)

‹#›

Japanese for Sign or Billboard

Kanban

Key Kanban concepts:
Visualize workflow
Kanban boards
Prioritize work
Limit work In Progress
Measure and manage flow
Cards
Tasks to be assigned and completed during an iteration

‹#›

Scrum

‹#›

[Pressman]



Scrum Meeting

TODO: Find 1 or 2 other students in class to complete another stand-up meeting!
What I did.
What I need to do next.
What is blocking me.
\* Share since last class, standing optional

‹#›

Lean Software Development

Agile-based framework focused on optimizing development time and resources

7 Principles
1. Eliminate Waste
2. Build Quality In
3. Create Knowledge
4. Defer Commitment
5. Deliver Fast
6. Respect People
7. Optimize the Whole

‹#›

[Poppendieck]

Crystal Agile Framework

Human-powered, adaptive, and ultra-light (little to no documentation) agile framework

7 Principles
1. Frequent Delivery
2. Reflective Improvement
3. Osmotic Communication
4. Personal Safety
5. Focus (on Work)
6. Easy Access to Expert Users
7. Technical Environment 

‹#›

 [Cockburn]

Agile Project Management

Agile-Inspired Project Meetings:
Stand-ups/Scrum Meeting ✅
Daily <15 min. meetings to provide updates on tasks
Sprint planning meetings
Triages
Sprint review meetings
Retrospectives
Will differ based on company, development team, etc.

‹#›

Sprint Planning

Meeting to review backlog and determine tasks to be completed in the upcoming sprint
Entire team (Scrum master, manager, developers, etc.)
Divide work between team members
How do you divide work between software engineers?[Wilson]
Feature decomposition- by feature aspects
Modular decomposition- by module (i.e. parts of code)
Functional decomposition- by set of tasks or skill
Rotating decomposition- by function, but swapping periodically
Chaotic decomposition- random
Project Estimation

‹#›

Sprint Planning: Backlog

https://www.visualstudio.com/en-us/docs/work/backlogs/create-your-backlog

‹#›

Sprint Planning: Project Estimation

Software projects require…
Size estimation
Effort estimation
Time estimation
Cost estimation
But, humans are mostly bad at estimation…

‹#›

Estimation techniques
Constructive Cost Model (COCOMO) [Boehm]
Planning Poker 🂡
Function points: estimated measure of time, effort, etc. to complete a work task

Ex) How many miles are between the Earth and the moon?
238,900 mi 🌎 🌘

Triage Meetings

Review of bugs and defects
Analyze reproducibility
Prioritize fixes
NOT coming up with a solution
Depending on team, triages can be regularly scheduled, integrated with sprint planning meetings, or only held in case of emergency.

‹#›

Sprint Review Meeting

Development team presents work that was completed during the sprint.
Often includes a demo of completed features, tasks
Collect immediate feedback from stakeholders
Anti-patterns [Wolpers]
Powerpoint presentation
No clients, stakeholders, or customers in attendance
Requirements analysis and specification
Wizard of Oz’ing
Extended scrum or planning meeting
Retrospective

‹#›

Retrospectives

Review of the sprint to reflect on activities and processes, brainstorm for next sprint.
Opportunity for Scrum team to inspect itself over the last sprint only!
Iterative improvement applied to the team
Retrospective questions:
What went well?
What didn’t go well?
What should we do differently next time?

‹#›

Caution! ⚠

There is no perfect software engineering process…
Agile development is not the silver bullet!
The First Law
“No matter where you are in the system life cycle, the system will change, and the desire to change it will persist throughout the life cycle.”
[Bersoff, 1980]

‹#›





[Pressman]

‹#›

‹#›



‹#›

How Does AI Fit In?

A goal of AI programming assistants is to enhance software development and productivity
i.e., streamline processes
However, there are mixed perceptions of how generative AI impacts SE processes.



‹#›

AI + Agile

The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed
James Ryseff, Brandon De Bruhl, Sydne J. Newberry

‹#›

Interviewed participants (5+ years of experience)
Key Finding: “Interestingly, several AI specialists see formal agile software development practices as a roadblock to successful AI.” [McKendrick]

AI + Agile (cont.)

“While the agile software movement never intended to develop rigid processes…[an interviewee said] work items repeatedly had to either be reopened in the following sprint or made ridiculously small and meaningless to fit into a one-week or two-week sprint. In particular, AI projects require an initial phase of data exploration and experimentation with an unpredictable duration. Interviewees recommended that instead of adopting established software engineering processes—which often amount to nothing more than fancy to-do lists—the technical team should communicate frequently with their business partners about the state of the project…Ultimately, organizations will need to rediscover how to make the agile software development process be adaptive and—truly—agile”.

‹#›

Software Engineering?

‹#›

“ ‘It’s Engineering... but not as we know it’… Software Engineering - solution to the software crisis, or part of the problem? ”

[Bryant]

Version Control

Version Control: Software that keeps track of changes to a set of files.
You likely use version control all the time outside of code:
In Microsoft Word you can use Ctrl+Z to undo changes (and go back to an earlier version of the document), in Google Docs you can see who made what changes to a file,...
Different implementations of version control for software development: Git (i.e., GitHub, GitLab, etc.), Subversion, Mercurial
Subversion: One SVN server can hold many repositories, one repository can hold many projects
Git: Distributed version control, everyone has their own local version control repository

Repository Layout

Each project has multiple revisions
Each revision is assigned a name
Revision number is incremented for every commit transaction
Delta (diff) information is recorded





Basic Features of a Repository

Keep the history of all changes to files and directories
– You can add in new versions
– You can recover any previous version
Access control
– Read/write permission for users
Logging
– Author, date, and reason for a change
Additional features
– Diff, Branches, Merging

Basic Workflow

The simplest way to use git is the “linear” workflow:
git init to enable Git in a certain directory
git add any files you want Git to “track”
git commit the currently “staged” changes to save a snapshot
make changes to your files
git add the changed files to “stage” them again
Repeat #3 (git commit)
Retrieve changes with git pull
You can use git log to see your commit history, and git status to see the current state of staged/unstaged changes.





Branching Workflow

You can split repos into branches, allowing people can work on different things without interfering with one another.
Make sure your repository is “clean” (i.e., no uncommitted changes).
git checkout -b to create a new branch and move to it; at this point, the new branch is identical to the old one.
Make changes, git add, git commit as usual (linear flow)
git checkout to switch between branches
Merging!

Branching

A branch is a mechanism for allowing concurrent changes to be made to a source repository.
Empirical research shows branching is effective, but developers create ineffective branches. [Bird]

‹#›

Branching (cont.)

Reasons to Branch:
Separate concerns among teams/developers
Tentative new features
Parallel version history without interference
Different releases
Fix bugs
…

‹#›

Branching Anti-patterns

Merge-a-phobia — avoiding merging at all cost, usually because of a fear of the consequences.
Merge Mania — spending too much time merging code instead of developing it.
Big Bang Merge — deferring branch merging and attempting to merge all branches simultaneously.
Never-Ending Merge — continuous merging activity because there is always more to merge.
Branch-a-holic — creating too many branches.
Cascading Branches — branching but never merging back to the main line.
Volatile Branches — branching with unstable files merged into other branches.
Development Freeze — stopping all development activities while branching and merging.
Integration Wall — using branches to divide the development team members, instead of dividing work.
Spaghetti Branching — integrating changes between unrelated branches. [Appleton]

‹#›

Merging Workflows

Now that we have multiple branches, we probably want to join them back together at some point. There are several ways to do this. Some include:
git merge
git cherry-pick
git rebase

Basic Merge Example

‹#›

Basic Merge Example

‹#›

Basic Merge Example



‹#›

Basic Merge Example



‹#›

Basic Merge Example



‹#›

Basic Merge Example



‹#›

Basic Merge Example

‹#›

Pull Requests

In reality, it’s very rare to merge branches locally and push them to remote. Instead, we use a service like GitHub or GitLab to help us:
Step 1: Create a fork (your own copy)
Step 2: Clone repo locally
Step 3: Create branch and make some commits
Step 4: Push those commits to your branch
Step 5: Open a pull/merge request
Step 6: Collaborate, leave comments, fix issues, etc. (code reviews)
Step 7: Merged into main (or other branch) by maintainer
Version Control System handles branching and merging under the hood.

Next Class

1/27: Software Engineering Basics Workshop
Requires Docker Labspace (see HW0)
1/29: Guest Lecture
David Bates, Ozmo Head of Innovation
Announcements
HW0 due 1/30 before midnight
Syllabus questions, Introduction, Class setup and configuration checks

‹#›

References

Joe McKendrick. “AI development and agile don't mix well, study shows”. ZDNet, 2024.
Mark Samuels. “Agile development can unlock the power of generative AI - here's how”. ZDNet, 2024.
Brad Appleton, Steve Berczuk, Ralph Cabrera, and Robert Orenstein. "Streamed lines: Branching patterns for parallel software development." In Proceedings of PloP, vol. 98, p. 14. 1998.
Emad Shihab, Christian Bird, and Thomas Zimmermann. "The effect of branching strategies on software quality." In Proceedings of the ACM-IEEE international symposium on Empirical software engineering and measurement, pp. 301-310. 2012.
Computer Hope, "Computer Programming History".
An extract from the entry on software engineering, a subsection of the entry on Computer Science: Software, in the CDROM version of the Encyclopaedia Britannica, as quoted by: A Bryant, "'It's Engineering Jim ... but not as we know it' Software Engineering -solution to the software crisis, or part of the problem?", ACM.
James Ryseff, Brandon De Bruhl, Sydne J. Newberry. “The Root Cause of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI”. Rand, 2024
Mary Poppendieck and Tom Poppendieck. “Lean Software Development: An Agile Toolkit”. 2003
Roger Pressman. “Software Engineering: A Practitioner’s Approach”. McGraw Hill.
Kevin Juhasz. “The history of coding and software engineering”. Hack Reactor, 2020.
Tom Coshow and Arnold Gao. “Top Strategic Technology Trends for 2025: Agentic AI”. Gartner, IBM, 2024.
Na Meng and Barbara Ryder, Virginia Tech
Chris Parnin, NC State
Sarah Heckman, NC State

‹#›

References

Akshay Srivatsan, Ayelet Drazen, Jonathan Kula. “CS 45, Lecture 9 Version Control I”. Stanford.
Aaron Perley. “98-174 F17 Modern Version Control with Git”. Carnegie Mellon University.
Josh Ervin and Hunter Schafer. “Version Control and Git”. University of Iowa
Gustavo Pinto, Clarice Ferreira, Cleice Souza, Igor Steinmacher, Paulo Meirelles. “Training Software Engineers using Open-Source Software: The Students’ Perspective”. International Conference on Software Engineering, Software Engineering Education and Training track (ICSE-SEET). 2019
Fabio Santos and Bianca Trinkenreich. “Beyond the Job Posting: What Hiring Managers Seek in Entry-Level Software Engineering Candidates”. Empirical Software Engineering and Measurement (ESEM) Industry, Government, and Community track, 2025.
Helene G. Kershner. “Open Source Software”. University of Buffalo, 2008.
Open Source Initiative (OSI). http://www.opensource.org/
Synopsys. “Open Source Security and Risk Analysis Report”. 2023 https://www.pwc.com/us/en/services/consulting/library/gdpr-readiness.html
David A. Wheeler. “Why Free-Libre / Open Source Software (FLOSS)? Look at the Numbers!”. 2015. https://dwheeler.com/oss\_fs\_why.html

‹#›

