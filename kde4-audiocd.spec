Name:		kde4-audiocd
Version:	4.10.2
Release:	1
Epoch:		3
Summary:	KDE I/O Slave for Audio CDs
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/audiocd-kio
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/audiocd-kio-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	cdda-devel
Buildrequires:	libkcddb-devel
Buildrequires:	libkcompactdisc-devel
Conflicts:	kdemultimedia4-core < 3:4.5.71

%description
KDE I/O Slave for Audio CDs.

%files
%{_kde_libdir}/kde4/kcm_audiocd.so
%{_kde_libdir}/kde4/kio_audiocd.so
%{_kde_libdir}/kde4/libaudiocd_*
%{_kde_datadir}/config.kcfg/audiocd_*
%{_kde_services}/audiocd.desktop
%{_kde_services}/audiocd.protocol
%{_kde_appsdir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_kde_appsdir}/solid/actions/solid_audiocd.desktop
%{_kde_docdir}/HTML/en/kioslave/audiocd

#------------------------------------------------------------------------------

%define audiocdplugins_major 4
%define libaudiocdplugins %mklibname audiocdplugins %{audiocdplugins_major}

%package -n %{libaudiocdplugins}
Summary:	KDE I/O Slave for Audio CDs library
Group:		System/Libraries

%description -n %{libaudiocdplugins}
KDE I/O Slave for Audio CDs library using cdparanoia.

%files -n %{libaudiocdplugins}
%{_kde_libdir}/libaudiocdplugins.so.%{audiocdplugins_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libaudiocdplugins} = %{EVRD}
Conflicts:	kdemultimedia4-devel < 3:4.8.95

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/libaudiocdplugins.so
%{_kde_includedir}/*

#--------------------------------------------------------------------

%prep
%setup -qn audiocd-kio-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0
- Update files

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Wed Jul 11 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.95-1
+ Revision: 808860
- imported package kde4-audiocd

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Follow upstream and move kde4-audiocd from kdemultimedia4 to own packageset

