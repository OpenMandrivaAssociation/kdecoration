%define major 5
%define libname %{mklibname kdecorations2 %{major}}
%define devname %{mklibname kdecorations2 -d}
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for handling window decorations
Name:		kdecoration
Version:	5.27.3
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(ECM)

%package -n %{libname}
Summary:	KDE Decorations Library
Group:	System/Libraries
Obsoletes:	%{mklibname kdecorations2private 7} < %{EVRD}

%description -n %{libname}
KDE Decorations library

%files -n %{libname} -f %{name}.lang
%{_libdir}/libkdecorations2.so.%{major}*
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
%{_includedir}/KF5/kdecoration2_version.h
%{_includedir}/KDecoration2
%{_libdir}/*.so
%{_libdir}/cmake/KDecoration2

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name}
