# GPRename — Modern Pyhon GTK 4 Rewrite

   ___   ___  __
  / _ \ / _ \/__\ ___ ____   ____ ________   ___
 / /_\// /_)/ \/// _ \  _ \ / _  |  _   _ \ / _ \
/ /_\\/ ___/ _  \  __/ | | | (_| | | | | | |  __/
\____/\/   \/ \_/\___|_| |_|\__,_|_| |_| |_|\___|

 ***********************************************

This source tree is a complete rewrite of the supplied GPRename (version 2023-04-29) program for modern Linux.

---

GPRename is a complete batch renamer for files and directories.

Original copyright (C) 2001 gprename-users@lists.sourceforge.net

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
file COPYING that came with this software for details.

Home Page       - https://github.com/cdobrich/gprename
Wikipedia       - https://en.wikipedia.org/wiki/GPRename

## What Changed

The original program was a Perl application using `Gtk3.pm` and the GTK 3
Perl bindings. The supplied error:

    Can't locate Gtk3.pm in @INC ...

is therefore not treated as a package-management problem.

The application has been rewritten in **Python 3 with GTK 4 / PyGObject**.
The old Perl GUI is not used, and the source contains no `use Gtk3`,
`Gtk3::`, Perl `Glib`, or CPAN dependency.

The rewrite also removes obsolete GTK 3 widgets such as `GtkTreeView`,
`GtkMenuBar`, `GtkTable`, and the GTK 3 event-loop construction. The
filesystem browser uses GTK 4's `Gtk.TreeListModel`/`Gtk.ListView`, menus use
Gio actions and `Gtk.PopoverMenuBar`, and dialogs are GTK 4 windows.

## Retained GPRename Functions

- File and directory batch renaming.
- Case conversion:
  - ALL UPPERCASE
  - all lowercase
  - CamelCase
  - Only the first letter
  - Only The First Letter And After
- Insert text at a position.
- Delete a range.
- Replace/remove text.
- Literal and regular-expression replacement.
- `:1`, `:2`, ... regular-expression capture references.
- Numeric renaming with prefix/suffix and increment.
- Zero auto-fill.
- Keep original names before or after generated numbers.
- Preview.
- Multi-selection.
- Undo.
- Hidden-file display.
- Filename/path filter.
- Show path.
- Automatic preview.
- Remember last directory.
- Fullscreen.
- Rename safety checking.
- Log viewing and clearing.
- Command-line path opening.
- Desktop entry and manual page.
- XDG configuration directory support.

## Safer Rename Implementation

The original program performed each rename through `<name>_gp`. The rewrite
uses a unique temporary file in the destination directory for every selected
item, then completes the rename. This makes case-only changes and rename
cycles such as `a -> b` and `b -> a` work without overwriting an unrelated
file.

By default, destinations that already exist outside the selected rename set
are rejected. The security option remains available, but it should only be
used deliberately.

## Build and Install

    make
    sudo make install

The installed executable is:

    /usr/local/bin/gprename

A different prefix can be selected:

    sudo make install PREFIX=/usr

For a source-tree test, after the required modern GTK 4/PyGObject runtime is
available:

    ./src/gprename

The runtime requirements are intentionally limited to the modern GUI stack
used by the rewrite:

- Python 3
- GTK 4
- PyGObject (`gi.repository.Gtk` version 4.0)

No attempt is made to install or repair the obsolete Perl/Gtk3 dependency
chain.

## Different Languages

To run GPRename in another language, you need to open the application like so: `LANGUAGE=fr gprename`

The complete list of available languages is in the locale directory.

## Source preservation

The original project's translation `.po` files, license, icon, and historical
documentation can be retained alongside this source tree. The GTK 4 rewrite
uses gettext where a compiled `gprename` catalog is available and otherwise
falls back cleanly to English.
