Summary:	A graphical front end to the Red Hat Package Manager, for GNOME
Summary(pl):	Graficzny frontend pod GNOME do rpm
Name:		gnorpm
Version:	0.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.daa.com.au/pub/james/gnome/%{name}-%{version}.tar.gz
# Source0-md5:	fd5b10fb7beec852d844cd4b3bd3c53c
Patch0:		%{name}-redhat-config.patch
Patch1:		%{name}-rpm3.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	glint


%description
Gnome RPM is a graphical front end to RPM, similar to Glint, but
written with the GTK widget set and the GNOME libraries. It is
currently under development, so there are some features missing, but
you can currently query packages in the filesystem and database,
install upgrade, uninstall and verify packages.

%description -l pl
Gnome RPM jest graficznym interfejsem do RPM, podobnym do Glinta, ale
napisanym z u¿yciem widgetów GTK i bibliotek GNOME. Jest w trakcie
tworzenia, wiêc brakuje mu niektórych mo¿lio¶ci, ale aktualnie pozwala
pytaæ siê o pakiety w systemie plików i bazie danych, instalowaæ,
uaktualniaæ, odinstalowywaæ i weryfikowaæ pakiety.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
CFLAGSA="%{rpmcflags}" \
LDFLAGS="%{rpmldflags} -L%{_prefix}/lib" \
./configure \
	--prefix=%{_prefix} \
	--target=%{_target_platform} \
	--host=%{_host}
%{__make}

%find_lang %{name}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_bindir}/gnorpm
%{_datadir}/gnome/apps/*
%{_datadir}/gnome/help/gnorpm/C/*
# THIS SHOULD GO TO /etc !!!
%config %{_datadir}/gnorpmrc
#/usr/X11R6/share/pixmaps/defpackage.gif
