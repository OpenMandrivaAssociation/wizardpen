%define name wizardpen
%define version 0.7.0
%define release %mkrel 2

%define __libtoolize /bin/true

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wizardpen Driver for Linux
Group:		System/X11
License:	BSD/MIT
URL:		http://code.google.com/p/linuxgenius/
Source0:	http://linuxgenius.googlecode.com/files/wizardpen-%{version}-alpha2.tar.gz
Patch0:		wizardpen-xorg-1.7.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel
BuildRequires:	%{_lib}xext6-devel
BuildRequires:	x11-util-macros

%description
Wizardpen Driver for Linux.
What are referred to as "Genius Tablets" go by many names:

    * DigiPro 5x4 Graphics Tablet
    * Digital Ink Pad (A4 format)
    * G-pen
    * Genius Wizardpen
    * Genius Mousepen
    * Genius
    * iBall
    * Manhattan
    * Pentagram
    * QWare
    * Trust TB-3100
    * Trust TB-5300
    * Trust TB-6300
    * UC-LOGIC 

%prep
%setup -q -n %{name}-%{version}-alpha2
%patch0 -p1

%build
#autoreconf -fi
%configure2_5x --with-xorg-module-dir=%{_libdir}/xorg/modules/
%make

%install
rm -rf %{buildroot}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_libdir}/xorg/modules/input/wizardpen_drv.la
%{_libdir}/xorg/modules/input/wizardpen_drv.so
%{_mandir}/man4/wizardpen.4.lzma
