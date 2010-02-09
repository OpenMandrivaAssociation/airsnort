Summary:	A wireless LAN tool which cracks encryption keys
Name:		airsnort
Version:	0.2.7e
Release:	%mkrel 9
License:	GPLv2
Group:		Networking/Other
URL:		http://sourceforge.net/projects/airsnort/		
Source:		http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	libgnomeui2-devel
BuildRequires:	libpcap-devel >= 0.7.1-4mdk
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

