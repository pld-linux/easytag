# TODO:
#	fix desktop file encoding and Categories
# 
Summary:	ID3 tag editor
Summary(pl):	Edytor etykiet ID3
Name:		easytag
Version:	0.31
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/easytag/%{name}-%{version}.tar.bz2
# Source0-md5:	9cfb29a81f251891ec4dbae4cd39821d
Patch0:		%{name}-desktop.patch
URL:		http://easytag.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.1.0
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel      >= 1.2.7
BuildRequires:	id3lib-devel    >= 3.8.2
BuildRequires:	libogg-devel    >= 1.0
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC, OGG, MusePack and Monkey's Audio files. Its simple
and nice GTK+ interface makes tagging easier.

Features:
  - View, edit, write tags of MP3, MP2, FLAC files (supporting ID3v2 and
    ID3v1.x specifications), OGG files, MusePack and Monkey's Audio
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

%description -l pl
EasyTAG to narzêdzie do przegl±dania, modyfikowania i zapisywania
etykiet (tagów) w plikach MP3, MP2, FLAC, OGG, MusePack i Monkey's
Audio. Prosty i mi³y interfejs GTK+ u³atwia to zadanie.

Mo¿liwo¶ci:
 - przegl±danie, modyfikowanie, zapisywanie etykiet w plikach MP3,
   MP2, FLAC (z obs³ug± formatów ID3v2 i ID3v1.x), OGG, MusePack
   i Monkey's Audio
 - automatyczne etykietowanie: tworzenie pól na podstawie nazwy pliku
   i katalogu (przy u¿yciu masek)
 - mo¿liwo¶æ zmiany nazw plików na podstawie etykiet (przy u¿yciu
   masek) lub wczytuj±c je z pliku tekstowego
 - obróbka wszystkich plików w podanym katalogu
 - mo¿liwo¶æ przegl±dania podkatalogów
 - rekurencja przy etykietowaniu, usuwaniu, zmianie nazw, zapisywaniu
 - mo¿liwo¶æ ustawienia pola (wykonawca, tytu³...) we wszystkich
   pozosta³ych plikach
 - wczytywanie i wy¶wietlanie informacji z nag³ówka (czas, jako¶æ)
 - przegl±darka bazuj±ca na drzewie
 - lista z wyborem plików
 - prosty interfejs
 - generowanie playlist
 - wyszukiwanie plików.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO THANKS USERS-GUIDE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/easytag
%{_desktopdir}/*.desktop
%{_mandir}/man1/*.1*
%{_pixmapsdir}/*
