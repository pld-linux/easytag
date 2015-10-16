#
# Conditional build:
%bcond_without	nautilus	# nautilus context menu actions module
#
Summary:	ID3 tag editor
Summary(hu.UTF-8):	ID3 tag szerkesztő
Summary(pl.UTF-8):	Edytor etykiet ID3
Name:		easytag
Version:	2.4.0
Release:	2
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://ftp.gnome.org/pub/GNOME/sources/easytag/2.4/%{name}-%{version}.tar.xz
# Source0-md5:	5951c735cc997ac3e3d2b7a29da6c413
URL:		https://wiki.gnome.org/Apps/EasyTAG
BuildRequires:	appdata-tools
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd44-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	flac-devel >= 1.1.4
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	id3lib-devel >= 3.8.3
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libid3tag-devel
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libvorbis-devel >= 1:1.0.1
BuildRequires:	libxslt-progs
%{?with_nautilus:BuildRequires:	nautilus-devel >= 3.0}
BuildRequires:	opus-devel >= 1.0
BuildRequires:	opusfile-devel
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	speex-devel
BuildRequires:	taglib-devel >= 1.9.1
BuildRequires:	wavpack-devel >= 4.40
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	flac >= 1.1.4
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	libogg >= 2:1.0
Requires:	libvorbis >= 1:1.0.1
Requires:	opus >= 1.0
Requires:	taglib >= 1.9.1
Requires:	wavpack >= 4.40
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC, Ogg, MusePack and Monkey's Audio files. Its simple and
nice GTK+ interface makes tagging easier.

Features:
- View, edit, write tags of MP3, MP2, FLAC files (supporting ID3v2 and
  ID3v1.x specifications), Ogg files, MusePack and Monkey's Audio
- Auto tagging: parse filename and directory to complete automatically
  the fields (using masks),
- Ability to rename files from the tag (using masks) or by loading a
  txt file,
- Process all files of the selected directory,
- Ability to browse subdirectories,
- Recursion for tagging, removing, renaming, saving...,
- Can set a field (artist, title,...) to all other files,
- Read file header informations (bitrate, time, ...) and display them,
- A tree based browser,
- A list to select files,
- Simple and explicit interface!,
- A playlist generator window,
- A file searching window.

%description -l hu.UTF-8
EasyTag egy eszköz az MP3, MP2, FLAC, Ogg, MusePack és Monkey's Audio
fájlok tagjeinek megtekintésére, szerkesztésére és írására. Egy
egyszerű GTK+ felület ezt meg is könnyíti.

Lehetőségek:
- MP3, MP2, FLAC (ID3v2 és ID3v1.x is), Ogg, MusePack és Monkey's
  Audio fájlok tag-jeine megtekintése, szerkesztése és mentése
- Automatikus tag-szerkesztés: fájlnév és könyvtár feldolgozása
  alapján tölti ki a mezőket
- Fájlok átnevezése a mezők alapján vagy egy betöltött txt-fájl
  segítségével
- A kijelölt könyvtár összes fájljának feldolgozása
- Alkönyvtárak böngészése
- Rekurzió gyakorlatilag mindenre
- Összes fájlra mező beállítása (előadó, számcím)
- Header információk olvasása (bitráta, hossz, ...) és megjelenítése
- Fastruktúrás böngészés
- Fájlok listájának kijelölése
- Egyszerű és gyors felület
- Lejátszási lista generálás
- Fájlkeresés

%description -l pl.UTF-8
EasyTAG to narzędzie do przeglądania, modyfikowania i zapisywania
etykiet (tagów) w plikach MP3, MP2, FLAC, Ogg, MusePack i Monkey's
Audio. Prosty i miły interfejs GTK+ ułatwia to zadanie.

Możliwości:
- przeglądanie, modyfikowanie, zapisywanie etykiet w plikach MP3, MP2,
  FLAC (z obsługą formatów ID3v2 i ID3v1.x), Ogg, MusePack i Monkey's
  Audio,
- automatyczne etykietowanie: tworzenie pól na podstawie nazwy pliku i
  katalogu (przy użyciu masek),
- możliwość zmiany nazw plików na podstawie etykiet (przy użyciu
  masek) lub wczytując je z pliku tekstowego
- obróbka wszystkich plików w podanym katalogu,
- możliwość przeglądania podkatalogów,
- rekurencja przy etykietowaniu, usuwaniu, zmianie nazw, zapisywaniu
- możliwość ustawienia pola (wykonawca, tytuł...) we wszystkich
  pozostałych plikach,
- wczytywanie i wyświetlanie informacji z nagłówka (czas, jakość),
- przeglądarka bazująca na drzewie,
- lista z wyborem plików,
- prosty interfejs,
- generowanie playlist,
- wyszukiwanie plików.

%package -n nautilus-extension-easytag
Summary:	Nautilus extension to open files with EasyTAG
Summary(pl.UTF-8):	Rozszerzenie Nautilusa do otwierania plików w programie EasyTAG
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	nautilus >= 3.0.0

%description -n nautilus-extension-easytag
Nautilus extension to open directories and audio files with EasyTAG
using the context menu.

%description -n nautilus-extension-easytag -l pl.UTF-8
Rozszerzenie Nautilusa do otwierania katalogów i plików dźwiękowych w
programie EasyTAG przy użyciu menu kontekstowego.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_nautilus:--disable-nautilus-actions} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with nautilus}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/libnautilus-easytag.la
%else
%{__rm} $RPM_BUILD_ROOT%{_datadir}/appdata/easytag-nautilus.metainfo.xml
%endif

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/easytag
%{_datadir}/appdata/easytag.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.EasyTAG.gschema.xml
%{_desktopdir}/easytag.desktop
%{_mandir}/man1/easytag.1*
%{_iconsdir}/hicolor/*x*/apps/easytag.png
%{_iconsdir}/hicolor/scalable/apps/easytag.svg
%{_iconsdir}/hicolor/symbolic/apps/easytag-symbolic.svg

%if %{with nautilus}
%files -n nautilus-extension-easytag
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-easytag.so
%{_datadir}/appdata/easytag-nautilus.metainfo.xml
%endif
