%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE I/O Slave for Audio CDs
Name:		plasma6-audiocd-kio
Version:	24.01.85
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://projects.kde.org/projects/kde/kdemultimedia/audiocd-kio
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/audiocd-kio-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(KF6Cddb)
BuildRequires:	cmake(KF6CompactDisc)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KDELibs4Support)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cdda-devel
BuildRequires:	pkgconfig(libcdio_paranoia)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	lame
Conflicts:	kdemultimedia4-core < 3:4.6.71
Recommends:	lame

%description
KDE I/O Slave for Audio CDs.

%files -f all.lang
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

%define audiocdplugins_major 6
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
Conflicts:	kdemultimedia4-devel < 3:4.8.96

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde6_libdir}/libaudiocdplugins.so
%{_kde6_includedir}/*

#--------------------------------------------------------------------

%prep
%autosetup -p1 -n audiocd-kio-%{version}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
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
