%define major 5
%define libname %{mklibname kdecorations2 %{major}}
%define devname %{mklibname kdecorations2 -d}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library for handling window decorations
Name:		kdecoration
Version:	5.2.95
Release:	1
License:	LGPL
Group:		System/Libraries
Url:		http://kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake
BuildRequires:	ninja

%libpackage kdecorations2 %{major}

%libpackage kdecorations2private %{major}

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
%setup -q

%build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install

