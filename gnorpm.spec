Summary:	A graphical front end to the Red Hat Package Manager, for GNOME
Name: 		gnorpm
Version: 	0.8
Release: 	6
Copyright: 	GPL
Group: 		Applications/System
Source: 	ftp://ftp.daa.com.au/pub/james/gnome/gnorpm-%{version}.tar.gz
Patch0: 	gnorpm-redhat-config.patch
Patch1:		gnorpm-rpm3.patch
BuildRoot: 	/var/tmp/%{name}-%{version}-root
Obsoletes: 	glint

%description
Gnome RPM is a graphical front end to RPM, similar to Glint, but written with
the GTK widget set and the GNOME libraries.  It is currently under
development, so there are some features missing, but you can currently query
packages in the filesystem and database, install upgrade, uninstall and
verify packages.

%prep
%setup -q
%patch0 -p1
%patch1 -p0


%build
CFLAGSA="$RPM_OPT_FLAGS" \
LDFLAGS="-s -L/usr/X11R6/lib" \
./configure \
	--prefix=/usr/X11R6 \
	--target=%{_target_platform} \
	--host=%{_host}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/gnorpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/X11R6/bin/gnorpm
/usr/X11R6/share/gnome/apps/*
/usr/X11R6/share/gnome/help/gnorpm/C/*
/usr/X11R6/share/locale/*/LC_MESSAGES/gnorpm.mo
%config /usr/X11R6/share/gnorpmrc
#/usr/X11R6/share/pixmaps/defpackage.gif
%doc AUTHORS NEWS README

%changelog
* Mon Apr 12 1999 Matt Wilson <msw@redhat.com>
- updated to 0.8

* Fri Mar 12 1999 Matt Wilson <msw@redhat.com>
- patched to work with rpm-3.0
- GnoRPM obsoletes glint.
