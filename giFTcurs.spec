Name: giFTcurs
Summary: Cursed frontend to the giFT daemon
Version: 0.6.2
Release: 8
Source:  http://savannah.nongnu.org/download/giftcurs/%name-%version.tar.bz2
Source1: %{name}-icon-16.png
Source2: %{name}-icon-32.png
Source3: %{name}-icon-48.png
URL: http://www.nongnu.org/giftcurs/
Group: Networking/Other
License: GPL
BuildRequires:	glib2-devel
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(ncursesw)
Suggests: gift
# It doesn't not requires giFT to run 'cause it can connect to another
# host

%description
The giFTcurs software is a cursed frontend to the giFT daemon and has been
described as "seriously slick". It won't work that well without giFT, which
you should have already.

%prep
%setup -q

%build
%configure2_5x --with-ncursesw
%make

%install
%makeinstall_std
%find_lang %{name}

strip %{buildroot}%{_bindir}/giFTcurs

# menu
install %{SOURCE1} -D -m 644 %{buildroot}%{_miconsdir}/%{name}.png
install %{SOURCE2} -D -m 644 %{buildroot}%{_iconsdir}/%{name}.png
install %{SOURCE3} -D -m 644 %{buildroot}%{_liconsdir}/%{name}.png

# Creation of the menu item

mkdir -p %{buildroot}%{_datadir}/applications/

cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/giFTcurs
Categories=P2P;Network;FileTransfer;ConsoleOnly;
Name=GiFTcurs
Comment=Cursed frontend for the giFT peer2peer software
Icon=%{name}
Terminal=true
EOF

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README COPYING NEWS AUTHORS ChangeLog TODO ABOUT-NLS
%{_bindir}/giFTcurs
%{_datadir}/applications/mandriva-giFTcurs.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/man1/giFTcurs.1*
%{_mandir}/man5/giFTcurs.conf.5*



%changelog
* Fri Aug 12 2011 Andrey Bondrov <abondrov@mandriva.org> 0.6.2-7mdv2012.0
+ Revision: 694112
- imported package giFTcurs


* Fri Apr 12 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.6.2-7mdv2010.2
- Port to 2011
- Little spec clean up

* Sat Jan 19 2008 Anssi Hannula <anssi@zarb.org> 0.6.2-6plf2008.1
- XDG menu
- suggests gift instead of requiring it
- buildrequires gpm-devel
- build with ncursesw
