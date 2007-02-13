Summary:	A graphical front end to the Red Hat Package Manager, for GNOME
Summary(pl.UTF-8):	Graficzny frontend pod GNOME do rpm
Name:		gnorpm
Version:	0.98
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.virtualworlds.de/Download/%{name}-%{version}.src.tar.bz2
# Source0-md5:	b9175d65243b9a514ef3fdcee440ce3d
URL:		http://www.virtualworlds.de/GRPM/
Patch0:		%{name}-locale-zh.patch
#TODO correct patch1
Patch1:		%{name}-rpm.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libghttp-devel >= 1.0.3
BuildRequires:	libxml-devel >= 1.3
BuildRequires:	gtkhtml-devel
BuildRequires:	rpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	glint

%description
GNOME RPM is a graphical front end to RPM, similar to Glint, but
written with the GTK+ widget set and the GNOME libraries. It is
currently under development, so there are some features missing, but
you can currently query packages in the filesystem and database,
install upgrade, uninstall and verify packages.

%description -l pl.UTF-8
GNOME RPM jest graficznym interfejsem do RPM, podobnym do Glinta, ale
napisanym z użyciem widgetów GTK+ i bibliotek GNOME. Jest w trakcie
tworzenia, więc brakuje mu niektórych możliwości, ale aktualnie
pozwala pytać się o pakiety w systemie plików i bazie danych,
instalować, uaktualniać, odinstalować i weryfikować pakiety.

%prep
%setup -q
%patch0 -p1
#TODO correct this patch
#%patch1 -p1

mv -f po/{zh_TW.Big5,zh_TW}.po
mv -f po/{zh_CN.GB2312,zh_CN}.po

%build
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/System

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnorpm
%{_datadir}/mime-info/*
%{_applnkdir}/System/*.desktop
%{_pixmapsdir}/*.png
# THIS SHOULD GO TO /etc !!!
%config %{_datadir}/gnorpmrc
