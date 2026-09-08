# Modern GPRename build/install file.
#
# The old project installed a Perl/Gtk3 program.  This version installs a
# Python 3 + GTK 4 application and does not invoke CPAN, Gtk3.pm, or Perl.

PREFIX ?= /usr/local
DESTDIR ?=
BINDIR = $(DESTDIR)$(PREFIX)/bin
DATADIR = $(DESTDIR)$(PREFIX)/share
APPLICATIONDIR = $(DATADIR)/applications
ICONDIR = $(DATADIR)/icons/hicolor/48x48/apps
MANDIR = $(DATADIR)/man/man1

.PHONY: all install uninstall clean check

all: check

check:
	python3 -m py_compile src/gprename

install: check
	install -d "$(BINDIR)" "$(APPLICATIONDIR)" "$(ICONDIR)" "$(MANDIR)"
	install -m 755 src/gprename "$(BINDIR)/gprename"
	install -m 644 share/applications/gprename.desktop "$(APPLICATIONDIR)/gprename.desktop"
	install -m 644 share/icons/hicolor/48x48/apps/gprename.png "$(ICONDIR)/gprename.png"
	install -m 644 share/man/man1/gprename.1 "$(MANDIR)/gprename.1"
	@echo "GPRename installed to $(BINDIR)/gprename"

uninstall:
	rm -f "$(BINDIR)/gprename"
	rm -f "$(APPLICATIONDIR)/gprename.desktop"
	rm -f "$(ICONDIR)/gprename.png"
	rm -f "$(MANDIR)/gprename.1"

clean:
	rm -rf src/__pycache__
