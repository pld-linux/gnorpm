%define prefix /usr
%define ver    0.8

Summary: A graphical front end to the Red Hat Package Manager, for GNOME
Name: gnorpm
Version: %ver
Release: 0.1
Copyright: GPL
Group: Applications/System
Source: ftp://ftp.daa.com.au/pub/james/gnome/gnorpm-%{ver}.tar.gz
Patch0: gnorpm-redhat-config.patch
BuildRoot: /var/tmp/gnorpm-%{PACKAGE_VERSION}-root
Obsoletes: glint

%description
Gnome RPM is a graphical front end to RPM, similar to Glint, but written with
the GTK widget set and the GNOME libraries.  It is currently under
development, so there are some features missing, but you can currently query
packages in the filesystem and database, install upgrade, uninstall and
verify packages.

%prep
%setup -n gnorpm-%{ver}
%patch0 -p 1 -b .rhconfig

CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install
strip $RPM_BUILD_ROOT%{prefix}/bin/gnorpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{prefix}/bin/gnorpm
%{prefix}/share/gnome/apps/*
%{prefix}/share/gnome/help/gnorpm/C/*
%{prefix}/share/locale/*/LC_MESSAGES/gnorpm.mo
%config %{prefix}/share/gnorpmrc
#%{prefix}/share/pixmaps/defpackage.gif
%doc AUTHORS NEWS README

%changelog
* Mon Apr 12 1999 Matt Wilson <msw@redhat.com>
- updated to 0.8

* Fri Mar 12 1999 Matt Wilson <msw@redhat.com>
- patched to work with rpm-3.0
- GnoRPM obsoletes glint.
