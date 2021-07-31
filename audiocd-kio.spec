%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE I/O Slave for Audio CDs
Name:		audiocd-kio
Version:	21.07.90
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://projects.kde.org/projects/kde/kdemultimedia/audiocd-kio
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(KF5Cddb)
BuildRequires:	cmake(KF5CompactDisc)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	lame
Conflicts:	kdemultimedia4-core < 3:4.5.71
Recommends:	lame

%description
KDE I/O Slave for Audio CDs.

%files -f all.lang
%{_datadir}/qlogging-categories5/kio_audiocd.categories
%{_libdir}/qt5/plugins/libaudiocd_encoder_flac.so
%{_libdir}/qt5/plugins/libaudiocd_encoder_lame.so
%{_libdir}/qt5/plugins/libaudiocd_encoder_opus.so
%{_libdir}/qt5/plugins/libaudiocd_encoder_vorbis.so
%{_libdir}/qt5/plugins/libaudiocd_encoder_wav.so
%{_libdir}/qt5/plugins/kcm_audiocd.so
%{_libdir}/qt5/plugins/kf5/kio/audiocd.so
%{_datadir}/konqsidebartng/virtual_folders/services/audiocd.desktop
%{_datadir}/kservices5/audiocd.desktop
%{_datadir}/metainfo/org.kde.kio_audiocd.metainfo.xml
%{_datadir}/solid/actions/solid_audiocd.desktop
%{_datadir}/config.kcfg/audiocd_flac_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_lame_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_opus_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_vorbis_encoder.kcfg
%{_datadir}/qlogging-categories5/kio_audiocd.renamecategories

#------------------------------------------------------------------------------

%define audiocdplugins_major 5
%define libaudiocdplugins %mklibname audiocdplugins %{audiocdplugins_major}

%package -n %{libaudiocdplugins}
Summary:	KDE I/O Slave for Audio CDs library
Group:		System/Libraries

%description -n %{libaudiocdplugins}
KDE I/O Slave for Audio CDs library using cdparanoia.

%files -n %{libaudiocdplugins}
%{_libdir}/libaudiocdplugins.so.%{audiocdplugins_major}*

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
%{_kde5_libdir}/libaudiocdplugins.so
%{_kde5_includedir}/*

#--------------------------------------------------------------------

%prep
%setup -qn audiocd-kio-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang audiocd_encoder_flac
%find_lang audiocd_encoder_lame
%find_lang audiocd_encoder_opus
%find_lang audiocd_encoder_vorbis
%find_lang kcmaudiocd --with-html
%find_lang kio_audiocd
%find_lang audiocd --with-html
cat *.lang >all.lang
