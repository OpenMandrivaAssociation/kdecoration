%define major 6
%define libname %{mklibname kdecorations3}
%define devname %{mklibname kdecorations3 -d}
%define oldlibname %{mklibname kdecorations2_6}
%define olddevname %{mklibname kdecorations2_6 -d}
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Library for handling window decorations
Name:		kdecoration
Version:	6.4.4
Release:	%{?git:0.%{git}.}2
License:	LGPL
Group:		System/Libraries
Url:		https://kde.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kdecoration/-/archive/%{gitbranch}/kdecoration-%{gitbranchd}.tar.bz2#/kdecoration-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/kdecoration-%{version}.tar.xz
%endif
BuildRequires:	cmake(Qt6)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(ECM)
BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
# Renamed after 6.0 2025-05-01
%rename plasma6-kdecoration

%package -n %{libname}
%rename %{oldlibname}
Summary:	KDE Decorations Library
Group:	System/Libraries

%description -n %{libname}
KDE Decorations library

%files -n %{libname} -f %{name}.lang
%{_libdir}/libkdecorations3.so.*
%{_libdir}/libkdecorations3private.so.*

%description
Library for dealing with window decorations.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF6/kdecoration3_version.h
%{_includedir}/KDecoration3
%{_libdir}/*.so
%{_libdir}/cmake/KDecoration3
