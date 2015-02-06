%define name wizardpen
%define version 0.8.1
%define release 2

%define __libtoolize /bin/true

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wizardpen Driver for Linux
Group:		System/X11
License:	GPLv2+
URL:		https://launchpad.net/wizardpen
Source0:	http://launchpad.net/wizardpen/trunk/0.8/+download/xorg-input-%{name}-%{version}.tar.bz2
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel
BuildRequires:	pkgconfig(xorg-macros)

%description
Wizardpen Driver for Linux.
What are referred to as "Genius Tablets" go by many names:

    * DigiPro 5x4 Graphics Tablet
    * Digital Ink Pad (A4 format)
    * G-pen
    * EasyPen i405
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
%setup -q -n xorg-input-%{name}-%{version}

%build
#autoreconf -fi
%configure2_5x --with-xorg-module-dir=%{_libdir}/xorg/modules/
%make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc
%{_libdir}/xorg/modules/input/wizardpen_drv.so
%{_bindir}/wizardpen-calibrate
%{_datadir}/X11/xorg.conf.d/70-wizardpen.conf
%{_sysconfdir}/udev/rules.d/67-xorg-wizardpen.rules
%{_mandir}/man4/%name.*
