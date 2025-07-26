#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE I/O Slave for Audio CDs
Name:		audiocd-kio
Version:	25.04.3
Release:	%{?git:0.%{git}.}2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://projects.kde.org/projects/kde/kdemultimedia/audiocd-kio
%if 0%{?git:1}
Source0:	https://invent.kde.org/multimedia/audiocd-kio/-/archive/%{gitbranch}/audiocd-kio-%{gitbranchd}.tar.bz2#/audiocd-kio-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/audiocd-kio-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(KCddb6)
BuildRequires:	cmake(KCompactDisc6)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	lame
Recommends:	lame

%rename plasma6-audiocd-kio

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE I/O Slave for Audio CDs.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kio_audiocd.categories
%{_libdir}/qt6/plugins/libaudiocd_encoder_flac.so
%{_libdir}/qt6/plugins/libaudiocd_encoder_lame.so
%{_libdir}/qt6/plugins/libaudiocd_encoder_opus.so
%{_libdir}/qt6/plugins/libaudiocd_encoder_vorbis.so
%{_libdir}/qt6/plugins/libaudiocd_encoder_wav.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_audiocd.so
%{_libdir}/qt6/plugins/kf6/kio/audiocd.so
%{_datadir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/metainfo/org.kde.kio_audiocd.metainfo.xml
%{_datadir}/solid/actions/solid_audiocd.desktop
%{_datadir}/config.kcfg/audiocd_flac_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_lame_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_opus_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_vorbis_encoder.kcfg
%{_datadir}/qlogging-categories6/kio_audiocd.renamecategories
%{_datadir}/applications/kcm_audiocd.desktop

#------------------------------------------------------------------------------

%define audiocdplugins_major 5
%define oldlibname %mklibname audiocdplugins 5
%define libaudiocdplugins %mklibname audiocdplugins

%package -n %{libaudiocdplugins}
Summary:	KDE I/O Slave for Audio CDs library
Group:		System/Libraries
Obsoletes:	%{oldlibname} < 4:0

%description -n %{libaudiocdplugins}
KDE I/O Slave for Audio CDs library using cdparanoia.

%files -n %{libaudiocdplugins}
%{_libdir}/libaudiocdplugins.so.%{audiocdplugins_major}*

#--------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libaudiocdplugins} = %{EVRD}
%rename plasma6-audiocd-kio-devel

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_libdir}/libaudiocdplugins.so
%{_includedir}/*
