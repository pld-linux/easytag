Summary:	Tag editor for MP3 and OGG files.
Name:		easytag
Version:	0.20
Release:	1
License:	GPL
URL:		http://easytag.sourceforge.net/
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/easytag/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		Jerome Couderc <j.couderc@ifrance.com>
BuildRequires:	gtk+-devel      >= 1.2.7
BuildRequires:	id3lib-devel    >= 3.7.12
BuildRequires:	libogg-devel    >= 1.0
BuildRequires:	libvorbis-devel >= 1.0

%define    _prefix    /usr/X11R6

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
  - A file searching window,
  - Written in C and uses GTK+ 1.2 for the GUI.


%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
autoheader
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
cat > $RPM_BUILD_ROOT%{_applnkdir}/Multimedia/easytag.desktop <<EOF
[Desktop Entry]
Name=EasyTAG
Comment=An utility for viewing/editing MP3 and OGG tags with a GTK+ GUI.
TryExec=easytag
Exec=easytag
Icon=EasyTAG.xpm
Terminal=0
Type=Application
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL COPYING README TODO THANKS USERS-GUIDE
%prefix/bin/easytag
%prefix/share/gnome/apps/Multimedia/easytag.desktop
%{_sysconfdir}/X11/applnk/Multimedia/easytag.desktop
%prefix/share/pixmaps/*
%prefix/share/easytag/*
%prefix/share/locale/*/*/*
