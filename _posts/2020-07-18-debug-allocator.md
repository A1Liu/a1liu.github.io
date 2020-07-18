---
title: Debug Allocator for C
categories: [programming]
tags: [c,programming]
---
I've made a debug allocator for the C; hopefully this will make it easier for
NYU students to learn C and debug their C programs for CSO. The files are:

-  [`debug_allocator.h`](https://raw.githubusercontent.com/A1Liu/config/master/libs/c/debug_allocator.h)
   This is the file that defines the macros that make the allocator work; you'll
   want to include it in your projects with `#include "debug_allocator.h"`.
-  [`debug_allocator.c`](https://raw.githubusercontent.com/A1Liu/config/master/libs/c/debug_allocator.c)
   This is the implementation file; it calls `malloc` and `free`, while tracking
   file and line numbers of allocations.

### Features
These two files provide the following features

-  `malloc`, `free`, and `realloc` macros - These macros are defined in `debug_allocator.h`,
   and simply call `__debug_alloc`, `__debug_dealloc`, and `__debug_realloc` respectively,
   while also passing in the file and line number they were called at.
-  Allocation tracking - `debug_allocator.c` tracks all allocations made during
   the program's execution.
-  Defined unitialized/freed values - unitialized memory is initialized with the
   value `0xdatafaded` and freed memory is overwritten with `0xdeadbeef`
-  Oversized allocations and accompanying defined values - Every allocation made
   is over-allocated by 5x, and the extra space is used as a buffer below and above
   on either side. These regions are initialized to `0xaabcdeff`, and overwritten
   with `0xbadadded` on free.
-  `check` macro - This macro calls `__debug_check_alloc`, and makes sure that
   the given pointer is a valid reference to the heap. Additionally, it uses the
   allocation information given to give better error messages.

### How to Use
To use these files, first download them (and/or copy-paste them) into your project.
Usually C projects come with a source folder, often abbreviated `src`, so that's
where they should go. Then any time you need to use `malloc`, add the following
line near the beginning of the file:

```c
#include "debug_allocator.h"
```

Then, just use `malloc` normally! The macros will take care of the rest.


