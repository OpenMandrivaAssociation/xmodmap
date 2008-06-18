Name: xmodmap
Version: 1.0.3
Release: %mkrel 4
Summary: Utility for modifying keymaps and pointer button mappings in X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xmodmap program is used to edit and display the keyboard modifier map and
keymap table that are used by client applications to convert event keycodes
into keysyms.

It has been obsoloted by XKB.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1*
