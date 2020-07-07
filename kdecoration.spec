%define major 5
%define pmajor 7
%define libname %{mklibname kdecorations2 %{major}}
%define devname %{mklibname kdecorations2 -d}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for handling window decorations
Name:		kdecoration
Version:	5.19.3
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(ECM)

%define libname %{mklibname kdecorations2 %{major}}

%package -n %{libname}
Summary: KDE Decorations Library
Group: System/Libraries

%description -n %{libname}
KDE Decorations library

%files -n %{libname} -f %{name}.lang
%{_libdir}/libkdecorations2.so.%{major}*

%define oldplibname %{mklibname kdecorations2private 5}
%define plibname %{mklibname kdecorations2private %{pmajor}}

%package -n %{plibname}
Summary: KDE Decorations Library, private parts
Group: System/Libraries
%rename %{oldplibname}

%description -n %{plibname}
KDE Decorations library, private parts

%files -n %{plibname}
%{_libdir}/libkdecorations2private.so.%{pmajor}*
%{_libdir}/libkdecorations2private.so.5*

%description
Library for dealing with window decorations.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Requires:	%{mklibname kdecorations2private %{major}} = %{EVRD}

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
