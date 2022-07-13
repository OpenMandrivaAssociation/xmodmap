Name: xmodmap
Version: 1.0.11
Release: 1
Summary: Utility for modifying keymaps and pointer button mappings in X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmodmap program is used to edit and display the keyboard modifier map and
keymap table that are used by client applications to convert event keycodes
into keysyms.

It has been obsoloted by XKB.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1*
