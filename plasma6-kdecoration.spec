%define major 6
%define libname %{mklibname kdecorations2}
%define devname %{mklibname kdecorations2 -d}
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define git 20231014

Summary:	Library for handling window decorations
Name:		plasma6-kdecoration
Version:	5.240.0
Release:	%{?git:0.%{git}.}1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kdecoration/-/archive/master/kdecoration-master.tar.bz2#/kdecoration-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%endif
# Don't fight with Plasma 5 over libkdecorations2.so.5
Patch0:		kdecoration-bump-soname.patch
BuildRequires:	cmake(Qt6)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(ECM)

%package -n %{libname}
Summary:	KDE Decorations Library
Group:	System/Libraries

%description -n %{libname}
KDE Decorations library

%files -n %{libname} -f kdecoration.lang
%{_libdir}/libkdecorations2.so.*
%{_libdir}/libkdecorations2private.so.*

%description
Library for dealing with window decorations.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF6/kdecoration2_version.h
%{_includedir}/KDecoration2
%{_libdir}/*.so
%{_libdir}/cmake/KDecoration2

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kdecoration-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# FIXME we temporarily remove the Chinese translation here because
# it (and, strangely, none of the other translations) conflicts with
# the Plasma 5 version
rm -rf %{buildroot}%{_datadir}/locale/zh_CN

%find_lang kdecoration
