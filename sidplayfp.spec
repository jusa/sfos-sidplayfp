Name:       sidplayfp
Summary:    SID player
Version:    1.4.3
Release:    1
Group:      Applications/Multimedia
License:    GPL 2.0
URL:        https://sourceforge.net/p/sidplay-residfp/wiki/Home/
Source0:    %{name}-%{version}.tar.gz
Source1:    sidplayfp.conf
BuildRequires:  pkgconfig(libsidplayfp) >= 1.8
BuildRequires:  pkgconfig(libpulse-simple) >= 1.8

%description
Sidplayfp is a fork of sidplay2 born with the aim to improve the quality of emulating the 6581, 8580 chips and the surrounding C64 system in order to play SID music better.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

install -d %{buildroot}/%{_sysconfdir}/pulse/xpolicy.conf.d
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/pulse/xpolicy.conf.d

%files
%defattr(-,root,root,-)
%{_bindir}/stilview
%{_bindir}/sidplayfp
%{_mandir}/man1/sidplayfp.1.gz
%{_mandir}/man1/stilview.1.gz
%{_mandir}/man5/sidplayfp.ini.5.gz
%{_sysconfdir}/pulse/xpolicy.conf.d/sidplayfp.conf
