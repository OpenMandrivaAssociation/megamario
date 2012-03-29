Name:		megamario
Version:	1.7
Release:	1
Summary:	Super Mario Bros 1 clone
Group:		Games/Arcade
License:	LGPL+
URL:		http://mmario.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mmario/MegaMario_v%{version}_full.zip
Source1:	%{name}.desktop
Patch0:		megamario-1.5-compile-fix.patch
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme

%description
MegaMario is a clone of the well know platform game Super Mario Bros 1.
In the game you play Mario, and your task is to free his brother Luigi,
who was captured by the evil Bowser.


%prep
%setup -q -c
%patch0 -p1
sed -i 's/\r//' *.txt

%build
make %{?_smp_mflags} PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
convert -transparent '#FF00FF' data/gfx/characters/small/player1r.PNG %{name}.png

%install
make install PREFIX=%{buildroot}%{_prefix}
# cruft removal
rm %{buildroot}%{_datadir}/megamario/levels/1/1
rm %{buildroot}%{_datadir}/megamario/levels/11/mai
rm %{buildroot}%{_datadir}/megamario/save.sav

# below is the desktop file and icon stuff.
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files
%doc CONTROLS.txt readme.txt fixes_v%{version}.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


