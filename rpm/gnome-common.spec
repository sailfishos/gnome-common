Name:           gnome-common
Version:        3.18.0
Release:        1
Summary:        Useful things common to building gnome packages from scratch
BuildArch:      noarch
License:        GPLv2
URL:            http://developer.gnome.org
Source0:        %{name}-%{version}.tar.xz

# This will pull in the latest version; if your package requires something older,
# well, BuildRequire it in that spec.  At least until such time as we have a
# build system that is intelligent enough to inspect your source code
# and auto-inject those requirements.
Requires: automake
Requires: autoconf
Requires: autoconf-archive
Requires: libtool
Requires: gettext
Requires: pkgconfig

%description
This package contains sample files that should be used to develop pretty much
every GNOME application.  The programs included here are not needed for running
gnome apps or building ones from distributed tarballs.  They are only useful
for compiling from CVS sources or when developing the build infrastructure for
a GNOME application.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%autogen --with-autoconf-archive
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%{_bindir}/gnome-autogen.sh
%{_datadir}/aclocal/*

