Summary:	Toshiba laptop function key utility
Summary(pl):	Narz�dzie do obs�ugi klawisza funkcyjnego w laptopach firmy Toshiba
Name:		fnfx
Version:	0.2
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fnfx/%{name}-%{version}.tar.gz
# Source0-md5:	fb0b2a9d6c5446a4615d907a572fd541
Source1:	%{name}.init
URL:		http://fnfx.sf.net/
Requires(post,preun):   /sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FnFX enables owners of Toshiba laptops to change the LCD brightness,
control the internal fan and use the special keys on their keyboard
(Fn-x combinations, hot-keys). The internal functions will give the
possibility to map the Fn-Keys to functions like volume up/down, mute,
suspend to disk, suspend to ram and switch LCD/CRT/TV-out. These
functions heavily depend on the system and/or kernel configuration.
You will need at least a kernel (v2.4.x, v2.6.x) with ACPI and Toshiba
support (CONFIG_ACPI and CONFIG_ACPI_TOSHIBA).

%description -l pl
FnFx pozwala posiadaczom laptop�w firmy Toshiba na zmian� jasno�ci
wy�wietlacza LCD, sterowanie wewn�trznym wiatraczkiem i korzystanie z
klawiszy specjalnych na klawiaturze (kombinacji Fn-x, skr�t�w
klawiszowych). Wewn�trzne funkcje daj� mo�liwo�� mapowania kombinacji
Fn-klawisz na funkcje takie jak zmiana g�o�no�ci, wyciszenie,
suspend-to-disk, suspend-to-ram oraz prze��czanie LCD/CRT/TV-out. Te
funkcje w du�ym stopniu s� zale�ne od konfiguracji systemu i/lub
j�dra. Potrzebne jest co najmniej j�dro (2.4.x, 2.6.x) z obs�ug� ACPI
i Toshiby (CONFIG_ACPI i CONFIG_ACPI_TOSHIBA).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/rc.d/init.d}
install -d $RPM_BUILD_ROOT/etc/fnfx
install src/{fnfx,fnfxd} $RPM_BUILD_ROOT%{_sbindir}
install etc/{fnfxd.conf,keymap} $RPM_BUILD_ROOT/etc/fnfx
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/fnfx

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}
if [ -f /var/lock/subsys/%{name} ]; then
        /etc/rc.d/init.d/%{name} restart >&2
else
        echo "Run \"/etc/rc.d/init.d/%{name} start\" to start %{name} daemon." >&2
fi

%preun
if [ "$1" = "0" ]; then
        if [ -f /var/lock/subsys/%{name} ]; then
                /etc/rc.d/init.d/%{name} stop >&2
        fi
        /sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(754,root,root)  /etc/rc.d/init.d/%{name}

#%doc ChangeLog INSTALL AUTHORS README
