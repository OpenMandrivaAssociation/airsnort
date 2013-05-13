Summary:	A wireless LAN tool which cracks encryption keys
Name:		airsnort
Version:	0.2.7e
Release:	%mkrel 10
License:	GPLv2
Group:		Networking/Other
URL:		http://sourceforge.net/projects/airsnort/		
Source:		http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pcap-devel = 1.3.0-2 >= 0.7.1-4mdk
#Requires:	prism2-utils
Provides:	Airsnort
Obsoletes:	Airsnort
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AirSnort is a wireless LAN (WLAN) tool which cracks encryption
keys on 802.11b WEP networks. AirSnort operates by passively
monitoring transmissions, computing the encryption key when
enough packets have been gathered.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README README.decrypt TODO
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.7e-10mdv2011.0
+ Revision: 609956
- rebuild

* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2.7e-9mdv2010.1
+ Revision: 502677
- Fix licence and URL

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.2.7e-8mdv2010.0
+ Revision: 436634
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.7e-7mdv2009.1
+ Revision: 298229
- rebuilt against libpcap-1.0.0

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.2.7e-6mdv2009.0
+ Revision: 240421
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0.2.7e-4mdv2007.0
- rebuild

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.7e-3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Sun Feb 13 2005 Austin Acton <austin@mandrake.org> 0.2.7e-2mdk
- don't requires prism2-utils

* Mon Jan 10 2005 Stefan van der Eijk <stefan@mandrake.org> 0.2.7e-1mdk
- New release 0.2.7e

* Fri Jan 07 2005 Stefan van der Eijk <stefan@mandrake.org> 0.2.7d-1mdk
- New release 0.2.7d
- make rpmbuildupdate capable

* Sun Dec 26 2004 Stefan van der Eijk <stefan@mandrake.org> 0.2.7c-1mdk
- 0.2.7c

* Wed Sep 22 2004 Stefan van der Eijk <stefan@eijk.nu> 0.2.6-1mdk
- 0.2.6

* Tue Sep 14 2004 Stefan van der Eijk <stefan@eijk.nu> 0.2.5b-1mdk
- 0.2.5b

* Sun Apr 11 2004 Stefan van der Eijk <stefan@eijk.nu> 0.2.4a-1mdk
- 0.2.4a

* Mon Jan 05 2004 Stefan van der Eijk <stefan@eijk.nu> 0.2.3c-1mdk
- 0.2.3c
- BuildRequires

* Thu Oct 09 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.2a-2mdk
- fixed upgrade from old package(name changed in last release)
- requires prism2-utils
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

* Wed Sep 10 2003 Stefan van der Eijk <stefan@eijk.nu> 0.2.2a-1mdk
- 0.2.2a
- renamed package /Airsnort/airsnort/
- fixed typo in 0.2.1b-1mdk changelog

