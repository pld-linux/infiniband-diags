# NOTE: for versions > 2.1.0 see rdma-core.spec
Summary:	InfiniBand diagnostic tools
Summary(pl.UTF-8):	Narzędzia diagnostyczne InfiniBand
Name:		infiniband-diags
Version:	2.1.0
Release:	2.1
License:	BSD or GPL v2
Group:		Networking/Utilities
#Source0Download: https://github.com/linux-rdma/infiniband-diags/releases
Source0:	https://github.com/linux-rdma/infiniband-diags/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	134a1ddf31df7bc05ff81636f4e35779
Patch0:		%{name}-link.patch
URL:		https://www.openfabrics.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	docutils
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libibumad-devel
BuildRequires:	libtool
BuildRequires:	opensm-devel
BuildRequires:	pkgconfig
BuildRequires:	systemd-devel
BuildRequires:	udev-devel >= 1:218
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides InfiniBand diagnostic programs and scripts
needed to diagnose an IB subnet.

%description -l pl.UTF-8
Ten pakiet zawiera programy i skrypty diagnostyczne InfiniBand
potrzebne do diagnostyki podsieci IB.

%package libs
Summary:	InfiniBand diagnostic library
Summary(pl.UTF-8):	Biblioteka diagnostyczna InfiniBand
Group:		Libraries
Requires:	libibmad = %{version}-%{release}

%description libs
InfiniBand diagnostic library.

%description libs -l pl.UTF-8
Biblioteka diagnostyczna InfiniBand.

%package devel
Summary:	Header files for libibnetdisc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libibnetdisc
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	libibmad-devel >= %{version}-%{release}
Requires:	libibumad-devel
Requires:	opensm-devel

%description devel
Header files for libibnetdisc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libibnetdisc.

%package static
Summary:	Static libibnetdisc library
Summary(pl.UTF-8):	Statyczna biblioteka libibnetdisc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libibnetdisc library.

%description static -l pl.UTF-8
Statyczna biblioteka libibnetdisc.

%package -n libibmad
Summary:	OpenFabrics Alliance InfiniBand MAD library
Summary(pl.UTF-8):	Biblioteka OpenFabrics Alliance InfiniBand MAD
Group:		Libraries

%description -n libibmad
libibmad provides low layer InfiniBand functions for use by the IB
diagnostic and management programs. These include MAD, SA, SMP, and
other basic IB functions.

%description -n libibmad -l pl.UTF-8
libibmad to biblioteka udostępniająca niskopoziomowe funkcje
InfiniBand przeznaczone dla programów diagnostycznych i zarządzających
IB. Obejmuje MAD, SA, SMP i inne podstawowe funkcje IB.

%package -n libibmad-devel
Summary:	Header files for libibmad library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libibmad
Group:		Development/Libraries
Requires:	libibmad = %{version}-%{release}
Requires:	libibumad-devel

%description -n libibmad-devel
Header files for libibmad library.

%description -n libibmad-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libibmad.

%package -n libibmad-static
Summary:	Static libibmad library
Summary(pl.UTF-8):	Statyczna biblioteka libibmad
Group:		Development/Libraries
Requires:	libibmad-devel = %{version}-%{release}

%description -n libibmad-static
This package contains the static libibmad library.

%description -n libibmad-static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę libibmad.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-perl-installdir=%{perl_vendorlib}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/infiniband-diags

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n libibmad -p /sbin/ldconfig
%postun	-n libibmad -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_sbindir}/check_lft_balance.pl
%attr(755,root,root) %{_sbindir}/dump_fts
%attr(755,root,root) %{_sbindir}/dump_lfts.sh
%attr(755,root,root) %{_sbindir}/dump_mfts.sh
%attr(755,root,root) %{_sbindir}/ibaddr
%attr(755,root,root) %{_sbindir}/ibcacheedit
%attr(755,root,root) %{_sbindir}/ibccconfig
%attr(755,root,root) %{_sbindir}/ibccquery
%attr(755,root,root) %{_sbindir}/ibfindnodesusing.pl
%attr(755,root,root) %{_sbindir}/ibhosts
%attr(755,root,root) %{_sbindir}/ibidsverify.pl
%attr(755,root,root) %{_sbindir}/iblinkinfo
%attr(755,root,root) %{_sbindir}/ibnetdiscover
%attr(755,root,root) %{_sbindir}/ibnodes
%attr(755,root,root) %{_sbindir}/ibping
%attr(755,root,root) %{_sbindir}/ibportstate
%attr(755,root,root) %{_sbindir}/ibqueryerrors
%attr(755,root,root) %{_sbindir}/ibroute
%attr(755,root,root) %{_sbindir}/ibrouters
%attr(755,root,root) %{_sbindir}/ibstat
%attr(755,root,root) %{_sbindir}/ibstatus
%attr(755,root,root) %{_sbindir}/ibswitches
%attr(755,root,root) %{_sbindir}/ibsysstat
%attr(755,root,root) %{_sbindir}/ibtracert
%attr(755,root,root) %{_sbindir}/perfquery
%attr(755,root,root) %{_sbindir}/saquery
%attr(755,root,root) %{_sbindir}/sminfo
%attr(755,root,root) %{_sbindir}/smpdump
%attr(755,root,root) %{_sbindir}/smpquery
%attr(755,root,root) %{_sbindir}/vendstat
%dir %{_sysconfdir}/infiniband-diags
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/infiniband-diags/error_thresholds
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/infiniband-diags/ibdiag.conf
%{perl_vendorlib}/IBswcountlimits.pm
%{_mandir}/man8/check_lft_balance.8*
%{_mandir}/man8/dump_fts.8*
%{_mandir}/man8/dump_lfts.8*
%{_mandir}/man8/dump_mfts.8*
%{_mandir}/man8/ibaddr.8*
%{_mandir}/man8/ibcacheedit.8*
%{_mandir}/man8/ibccconfig.8*
%{_mandir}/man8/ibccquery.8*
%{_mandir}/man8/ibfindnodesusing.8*
%{_mandir}/man8/ibhosts.8*
%{_mandir}/man8/ibidsverify.8*
%{_mandir}/man8/iblinkinfo.8*
%{_mandir}/man8/ibnetdiscover.8*
%{_mandir}/man8/ibnodes.8*
%{_mandir}/man8/ibping.8*
%{_mandir}/man8/ibportstate.8*
%{_mandir}/man8/ibqueryerrors.8*
%{_mandir}/man8/ibroute.8*
%{_mandir}/man8/ibrouters.8*
%{_mandir}/man8/ibstat.8*
%{_mandir}/man8/ibstatus.8*
%{_mandir}/man8/ibswitches.8*
%{_mandir}/man8/ibsysstat.8*
%{_mandir}/man8/ibtracert.8*
%{_mandir}/man8/infiniband-diags.8*
%{_mandir}/man8/perfquery.8*
%{_mandir}/man8/saquery.8*
%{_mandir}/man8/sminfo.8*
%{_mandir}/man8/smpdump.8*
%{_mandir}/man8/smpquery.8*
%{_mandir}/man8/vendstat.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibnetdisc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibnetdisc.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibnetdisc.so
%{_libdir}/libibnetdisc.la
%{_includedir}/infiniband/ibnetdisc.h
%{_includedir}/infiniband/ibnetdisc_osd.h
%{_mandir}/man3/ibnd_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libibnetdisc.a

%files -n libibmad
%defattr(644,root,root,755)
%doc libibmad/{ChangeLog,README}
%attr(755,root,root) %{_libdir}/libibmad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibmad.so.5

%files -n libibmad-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibmad.so
%{_libdir}/libibmad.la
%{_includedir}/infiniband/mad.h
%{_includedir}/infiniband/mad_osd.h

%files -n libibmad-static
%defattr(644,root,root,755)
%{_libdir}/libibmad.a
