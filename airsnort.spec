Summary:	A wireless LAN tool which cracks encryption keys
Name:		airsnort
Version:	0.2.7e
Release:	12
License:	GPLv2+
Group:		Networking/Other
Url:		http://sourceforge.net/projects/airsnort/
Source:		http://ovh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pcap-devel
BuildRequires:	pkgconfig(libgnomeui-2.0)

%description
AirSnort is a wireless LAN (WLAN) tool which cracks encryption
keys on 802.11b WEP networks. AirSnort operates by passively
monitoring transmissions, computing the encryption key when
enough packets have been gathered.

%files
%doc ChangeLog README README.decrypt TODO
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

