Summary:	InfiniBand diagnostic tools
Summary(pl.UTF-8):	Narzędzia diagnostyczne InfiniBand
Name:		infiniband-diags
Version:	1.6.0
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
# Source0-md5:	60c0e5365f1394ccc88d4f22ae2de09a
URL:		http://www.openfabrics.org/
BuildRequires:	libibmad-devel
BuildRequires:	libibumad-devel
BuildRequires:	opensm-devel
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

%description libs
InfiniBand diagnostic library.

%description libs -l pl.UTF-8
Biblioteka diagnostyczna InfiniBand.

%package devel
Summary:	Header files for libibnetdisc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libibnetdisc
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libibmad-devel
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

%prep
%setup -q

%build
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

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_sbindir}/check_lft_balance.pl
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
