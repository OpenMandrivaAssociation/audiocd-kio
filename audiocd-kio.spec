%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE I/O Slave for Audio CDs
Name:		audiocd-kio
Version:	16.04.3
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://projects.kde.org/projects/kde/kdemultimedia/audiocd-kio
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	cdda-devel
BuildRequires:	libkcddb-devel
BuildRequires:	libkcompactdisc-devel
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(vorbis)
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
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
