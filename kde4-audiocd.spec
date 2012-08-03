Name:		kde4-audiocd
Version:	4.9.0
Release:	1
Epoch:		3
Summary:	KDE I/O Slave for Audio CDs
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/kde/kdemultimedia/audiocd-kio
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/audiocd-kio-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libcdda-devel
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
%{_kde_appsdir}/kconf_update/audiocd.upd
%{_kde_appsdir}/kconf_update/upgrade-metadata.sh
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

