Name:		fnfx
Version:	0.2
Release:	0.1
Summary:	Toshiba laptop function key utility
License:	GPL
URL:		http://fnfx.sf.net
Group:		System/Configuration/Hardware
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	fb0b2a9d6c5446a4615d907a572fd541
Source1:	%{name}.init
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires(pre):	rpm-helper
Requires(post):	rpm-helper

%description
FnFX enables owners of Toshiba laptops to change the LCD brightness,
control, the internal fan and use the special keys on their keyboard
(Fn-x combinations, hot-keys). The internal functions will give the
possibility to map the Fn-Keys to functions like volume up/down, mute,
suspend to disk, suspend to ram and switch LCD/CRT/TV-out. These
functions heavily depend on the system and/or kernel configuration.
You will need at least a kernel (v2.4.x, v2.5.x, v2.6.x) with ACPI and
Toshiba support (CONFIG_ACPI and CONFIG_ACPI_TOSHIBA).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_initrddir}}
install -d $RPM_BUILD_ROOT/etc/fnfx
install src/{fnfx,fnfxd} $RPM_BUILD_ROOT%{_sbindir}
install etc/{fnfxd.conf,keymap} $RPM_BUILD_ROOT/etc/fnfx
install %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/fnfx


%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%config(noreplace) %{_initrddir}/%{name}

#%doc ChangeLog INSTALL AUTHORS README
