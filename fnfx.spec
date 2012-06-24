Summary:	Toshiba laptop function key utility
Summary(de):	Toshiba Laptop Funktionstasten listener
Summary(pl):	Narz�dzie do obs�ugi klawisza funkcyjnego w laptopach firmy Toshiba
Name:		fnfx
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fnfx/%{name}-%{version}.tar.gz
# Source0-md5:	2487730494a8ff86d83d9cf7e6a67325
Source1:	%{name}.init
URL:		http://fnfx.sourceforge.net/
Requires(post,preun):	/sbin/chkconfig
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

%description -l de
FnFX erm�glicht es Toshiba Laptop Benutzern die Helligkeit des LCD
Bildschirms zu �ndern, den internen Fan zu steuern und die
Funktionstasten auf den Laptop zu aktievieren (Fn-x kombinationen).
Die internen Funktionen erlauben es die Lautst�rke h�cher/niedriger zu
stellen, Ton ausschalten, einfrieren zu RAM/Festplatte und den wechsel
zwischen LCD/CRT/TV-out. Diese Optionen h�ngen schwer von der system
und/oder Kernel konfiguration ab. Du wirst mindestens einen Kernel
(v2.4.x, v.2.6.x) mit ACPI und Toshiba Unterst�tzung (CONFIG_ACPI and
CONFIG_ACPI_TOSHIBA) ben�tigen.

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
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/rc.d/init.d,%{_sysconfdir}/fnfx,%{_bindir}}

install src/fnfxd $RPM_BUILD_ROOT%{_sbindir}
install src/fnfx $RPM_BUILD_ROOT%{_bindir}
install etc/{fnfxd.conf,keymap} $RPM_BUILD_ROOT%{_sysconfdir}/fnfx
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/fnfxd
%attr(755,root,root) %{_bindir}/fnfx
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}
%attr(754,root,root)  /etc/rc.d/init.d/%{name}
