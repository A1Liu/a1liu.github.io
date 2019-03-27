---
title: Linux Development
categories: [personal, linux]
tags: [linux]
---
I've started developing on Linux! Here's a recounting of some of the things I've learned,
in part because sharing information is important, and in part because I might forget
what I did.

### Initial Plan
I've been meaning to try using Linux for a while now. My plan was to buy a Chromebook,
and install [GalliumOS][gallium-os] on it. From there, I'd start downloading apps
and figure out a plan of attack for customizing it for maximum performance.

[gallium-os]: https://galliumos.org/

### First Steps
I researched a few models of Acer, Dell, and HP computers using [the guide on the
GalliumOS wiki][hardware-guide], and was just about to buy an Acer,
when my friend Alex basically said I could have his! He had an old Acer C720, and
basically just gave it to me, so that's what I'll be working with.

[hardware-guide]: https://wiki.galliumos.org/Hardware_Compatibility

So I started by installing GalliumOS; [the instructions on the wiki][install-guide]
is pretty great, but here's a few things I learned that weren't mentioned there.

[install-guide]: https://wiki.galliumos.org/Installing

*  **You can only edit the firmware if you're running ChromeOS** - The initial firmware
   that the laptop comes with can only be edited with the write screw unscrewed,
   but doing that prevents the hardware from booting up in legacy mode (which is
   what GalliumOS boots up in if you don't install fresh firmware beforehand). If
   you want to upgrade the firmware, you have to do it with ChromeOS installed.
*  **You should edit the firmware** - The initial firmware just makes booting your
   computer annoying; just install the firmware from [MrChromeBox.tech][mr-chromebox-tech].
   For the Acer C720, I used [this video][acer-c720-disassembly].
*  **You probably don't need to back up your computer** - ChromeOS is available
   online for free; you can reset your device at any time. Unless you stored important
   files on the chromebook, you don't need to back it up.

[mr-chromebox-tech]: https://mrchromebox.tech/#fwscript
[acer-c720-disassembly]: https://www.youtube.com/watch?v=BG4ZWbimONQ

### Packages

*  Zsh and Oh-my-zsh
*  NeoVim
*  GNOME Software

### Keyboard Stuff
The keyboard is set kinda weirdly; I wanted to change it to make the keys a little
more useful for using Vim.

*  [Keyboard][keyboard-rebinding]

[keyboard-rebinding]: http://www.fascinatingcaptain.com/projects/remap-keyboard-keys-for-ubuntu/

### Integrating with GNOME

*  [GNOME and Ubuntu][integrating-gnome]

[integrating-gnome]: http://www.webupd8.org/2016/03/use-gnome-318-google-drive-integration.html

*  Learning cross platform stuff, and POSIX commands; adding a config repo
*  Setting up GalliumOS
   *  Zsh
   *  Acer C720
      *  GNOME and terminal, finding answers for questions is hard
      *  Disassembly, legacy mode, etc
*  Second time's the charm: linux on a budget
   *  Acer C710
   *  DDR3 RAM

