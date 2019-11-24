---
title: Plan for a Declarative Language
categories: [bugs-nyu, yacs]
tags: [language-design]
---
This is a recap of my meeting with Laurie Giannisis on March 22, 2019.

## Summary
1. The current system can be best optimized by **streamlining the communication
   channel between the registrar and the individual departments with which it must
   communicate.** We currently need to use human validation/clarification to ensure that the
   information in the database agrees with the departments' intentions. Standardizing
   the language used to describe course prerequisites could reduce ambiguity and
   thus the rate at which clarification is required.
2. If standardized, the same communications that departments have with the registrar
   can be used to give YACS information as well, without any additional overhead to NYU.
   Additionally, **this would not introduce any security vulnerabilities into NYU
   architecture,** as the sections of these communications that YACS needs access
   to are already public and available online through NYU websites.
3. Currently, a team is working on building tools to streamline the communications
   mentioned above, both through an established syntax, and through a program
   to generate text descriptors from database data. **I'd like to join this team
   on a volunteer basis,** both to ensure that YACS can be compatible
   as quickly as possible, but also to help reduce time-to-launch.
4. In order to be more effective from a YACS standpoint, I'd also like to **speak
   to a department head who currently is responsible for communicating course information
   with the registrar.** Since any standardization of communication that we do
   directly affects the ability for department heads to write course information down,
   I'd like to ensure that the changes we make to the process are measured and meaningful;
   additionally, I'd like for them to be as easy as possible to transition into.

## Current Workflow
Currently, the workflow for getting prerequisites entered into NYU's database begins
with department heads and professors, who write documents with specifications for
courses to be entered to the system, usually written in some variant of plain english.
This information is sent to the registrar's office, where it is translated from
text into database requisite information. Thus:

1. Department heads write out, in text, the specifications for courses and their requisites.
2. Text that is sent to the registrar is entered into the system (PeopleSoft).

The second step, as I understand it, is pretty well streamlined already; the people
that do the data entry are familar with their tools, and if these tools have shortcomings,
they're low priority.
However, there currently isn't an automated process for the validation of the
first step, and so it relies on deliberate validation by the registrar; in the event
of errors or ambiguity, the registrar ultimately must defer to the departments for clarification
on the semantic meaning of the information they were sent. This process can be slow.
The registrar's office needs to wait for departments to respond to its questions
with clarifications, and because synchronization between offices is difficult,
this process can sometimes take a day or two.

<div class="page-break"></div>
## Proposal
My proposed solution is the following:

1. A structured language that can be read by a computer program,
   which department heads can install. Instead of getting an email back
   from the registrar, department heads get an error notification on their own
   computer.
2. A program to convert from structured language to a database representation in
   YACS of course prerequisites.
3. A program to convert from an NYU database representation to a strutured text
   representation for display to students (and also YACS)

As Laurie pointed out to me, NYU currently has people working on the third item.
**As this very closely aligns with my current proposal, I'd like to join this team.**
By being a part of the conversation, I can ensure that YACS will be compatible with
the system that this team is currently building, and to me the most useful way
for me to be part of the conversation is to be on the team making the final
decisions on the structured text that YACS ultimately consumes.

## Short-term Plan
To effectively execute the above proposal, I'd like to begin with the following:

1. A strong channel of communication with the team that is currently implementing
   the translator mentioned above (item 3 in proposal). Ideally this would be
   accomplished by adding me to the team itself; if this isn't possible, I'd still
   like to be able to get a seat at the table somehow.
2. Interviews with a few department heads. In order to design the structured
   language well, I'd like to talk to its target user base; the department heads
   that will have to write in it. If the transition process is more difficult for
   them than the process of explaining in plain english what they'd like a second
   time, then there'd be no reason for them to follow the language. I'd like for
   this process to reduce inconvenience, and that can only happen if everyone involved
   has a reason to participate.
3. Continued correspondence with the registrar and NYU administration. In order
   best integrate YACS into NYU's ecosystem, I'd like to maintain an open communication
   channel between YACS/BUGS-NYU and the office of the registrar.

From what I understand, **none of the above would require** giving me, or anybody else
associated with BUGS or YACS, **additional security clearance.**

