Summary:	Cursed frontend to the giFT daemon
Name:		giFTcurs
Version:	0.6.2
Release:	10
License:	GPLv2+
Group:		Networking/Other
Url:		http://www.nongnu.org/giftcurs/
Source0:	http://savannah.nongnu.org/download/giftcurs/%name-%version.tar.bz2
Source1:	%{name}-icon-16.png
Source2:	%{name}-icon-32.png
Source3:	%{name}-icon-48.png
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(ncursesw)
Suggests:	gift
# It doesn't not requires giFT to run 'cause it can connect to another
# host

%description
The giFTcurs software is a cursed frontend to the giFT daemon and has been
described as "seriously slick". It won't work that well without giFT, which
you should have already.

%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS ChangeLog TODO ABOUT-NLS
%{_bindir}/giFTcurs
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/man1/giFTcurs.1*
%{_mandir}/man5/giFTcurs.conf.5*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --with-ncursesw
%make

%install
%makeinstall_std

%find_lang %{name}

# menu
install %{SOURCE1} -D -m 644 %{buildroot}%{_miconsdir}/%{name}.png
install %{SOURCE2} -D -m 644 %{buildroot}%{_iconsdir}/%{name}.png
install %{SOURCE3} -D -m 644 %{buildroot}%{_liconsdir}/%{name}.png

# Creation of the menu item

mkdir -p %{buildroot}%{_datadir}/applications/

cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/giFTcurs
Categories=P2P;Network;FileTransfer;ConsoleOnly;
Name=GiFTcurs
Comment=Cursed frontend for the giFT peer2peer software
Icon=%{name}
Terminal=true
EOF

