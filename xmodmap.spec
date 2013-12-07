Name: xmodmap
Version: 1.0.8
Release: 2
Summary: Utility for modifying keymaps and pointer button mappings in X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
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
%makeinstall_std

%files
%{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1*


%changelog
* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.7-1
+ Revision: 794234
- version update 1.0.7

* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.6-1
+ Revision: 786813
- version update 1.0.6

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2
+ Revision: 671351
- mass rebuild

* Sun Sep 26 2010 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 581088
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.4-1mdv2010.1
+ Revision: 464745
- New version: 1.0.4

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.3-5mdv2009.1
+ Revision: 350882
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2009.0
+ Revision: 226069
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 154402
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-2mdv2008.0
+ Revision: 90386
- rebuild

* Tue Aug 07 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.3-1mdv2008.0
+ Revision: 59575
- new upstream release: 1.0.3

