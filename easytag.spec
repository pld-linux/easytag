# TODO: port to standalone mp4v2

%bcond_with	mp4v2		# build with mp4v2 support

Summary:	ID3 tag editor
Summary(hu.UTF-8):	ID3 tag szerkesztő
Summary(pl.UTF-8):	Edytor etykiet ID3
Name:		easytag
Version:	2.1.7
Release:	2
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/easytag/%{name}-%{version}.tar.bz2
# Source0-md5:	9df3e800d80e754670642f2ba5e03539
Patch0:		%{name}-desktop.patch
URL:		http://easytag.sourceforge.net/
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	id3lib-devel >= 3.8.3
BuildRequires:	libid3tag-devel
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libvorbis-devel >= 1:1.0
%{?with_mp4v2:BuildRequires:	mp4v2-devel}
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRequires:	wavpack-devel >= 4.40
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC, Ogg, MusePack and Monkey's Audio files. Its simple and
nice GTK+2 interface makes tagging easier.

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
egyszerű GTK+2 felület ezt meg is könnyíti.

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
Audio. Prosty i miły interfejs GTK+2 ułatwia to zadanie.

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

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	%{!?with_mp4v2:--disable-mp4}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO THANKS USERS-GUIDE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
%{_pixmapsdir}/*
