Summary:	Tag editor for MP3 and OGG files
Summary(pl):	Edytor etykiet plików MP3 i OGG
Name:		easytag
Version:	0.27
Release:	1
License:	GPL
Vendor:		Jerome Couderc <j.couderc@ifrance.com>
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/easytag/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_inclusion_patch_in_configurein.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-ac_fix.patch
URL:		http://easytag.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel      >= 1.2.7
BuildRequires:	id3lib-devel    >= 3.8.2
BuildRequires:	libogg-devel    >= 1.0
BuildRequires:	libvorbis-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC and OGG files. Its simple and nice GTK+ interface makes
tagging easier.

Features:
  - View, edit, write tags of MP3, MP2, FLAC files (supporting ID3v2 and
    ID3v1.x specifications) and OGG files,
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
EasyTAG to narzêdzie do przegl±dania, modyfikownia i zapisywania
etykiet (tagów) w plikach MP3, MP2, FLAC i OGG. Prosty i mi³y
interfejs GTK+ u³atwia to zadanie.

Mo¿liwo¶ci:
 - przegl±danie, modyfikowanie, zapisywanie etykiet w plikach MP3,
   MP2, FLAC (z obs³ug± formatów ID3v2 i ID3v1.x) i OGG
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
 - prosty inferfejs
 - generowanie playlist
 - wyszukiwanie plików.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
#%patch2 -p0

%build
rm -f missing
%{__gettextize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnome_menudir=%{_applnkdir}/Multimedia

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README TODO THANKS USERS-GUIDE
%attr(755,root,root) %{_bindir}/easytag
%{_applnkdir}/Multimedia/easytag.desktop
%{_pixmapsdir}/*
%{_datadir}/easytag
%{_mandir}/man1/*.1*
