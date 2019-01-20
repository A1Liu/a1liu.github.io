---
title: BUGS Webpage Bootstrap Refactor
categories: [bugs-nyu, webpage, bootstrap]
tags: [html, css, sass, bootstrap]
---
<!-- {% raw %} -->
<!-- {% include refc-small.html text="ref commit" commit="3cad96569b964c415cd98a3b66aed73c01d87113" %} -->
<!-- {% include ref-commit.html text="text" commit="29e6933aa4512f36e6f85668d28a69b3f58678b8" %} -->
<!-- {% endraw %} -->
So I'm going to try to refactor the code in the repository to be more manageable.
Like right now we don't use bootstrap, so a lot of our SASS code is probably redundant.
Also, in general our stuff seems kinda verbose;
ideally we want reduce repetition of information as much as possible.
More specifically, what this refactor is supposed to accomplish:

Make the website...
1. Easier to read for people that haven't worked on this website in the past to understand
the code
2. More scalable in terms of project size/code line count
3. Modular to reduce time to fix in the future
4. A resource to learn from

I doubt that I'll be able to accomplish all of the above, but I think they're good
principals to keep in mind.
I'm mostly focusing on 1., but I think there's some overlap between that and the other
goals so hopefully I'll do a little bit of all of them.

#### Jan 23, 2019
## Documentation Pre-Bootstrap
Documenting the way HTML and CSS interact with each other in the webpage,
and where HTML and CSS is stored in the repository

#### Feb 5, 2019
## Implementing the Bootstrap Grid System
First step is to rewrite the site in the language of Bootstrap,
using the [Bootstrap grid system][grid-system].

[grid-system]: https://getbootstrap.com/docs/4.0/layout/grid/

### Planning Phase

### Implementation Overview

#### Feb 7, 2019
## Documentation, Post-Bootstrap

#### Feb 15, 2019
## Tying Up Loose Ends and Release
