Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Name:		bc
Version:	1.06.95
Release:	14
License:	GPLv2+ 
URL:		http://www.gnu.org/software/bc/bc.html
Group:		Sciences/Mathematics
Source0:	http://alpha.gnu.org/gnu/bc/%{name}-%{version}.tar.bz2
# Fedora patches
# dc accepts the input which contains wrong symbols of radix in same way like bc (RH bug#151844)
Patch1:		bc-1.06-dc_ibase.patch
# fix small memory leak (gentoo patch)
Patch2:		bc-1.06.95-memleak.patch
BuildRequires:	flex
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	bison
Requires(post):	grep
Requires(preun):	grep

%description
The bc package includes bc and dc.  Bc is an arbitrary precision numeric
processing arithmetic language.  Dc is an interactive arbitrary precision
stack based calculator, which can be used as a text mode calculator.

Install the bc package if you need its number handling capabilities or
if you would like to use its text mode calculator.

%prep
%setup -q
%patch1 -p1 -b .dc_ibase
%patch2 -p1 -b .memleak

%build
%configure2_5x \
		--with-readline

%make

%install
%makeinstall_std


%files
%doc FAQ AUTHORS NEWS README
%{_bindir}/bc
%{_bindir}/dc
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%{_infodir}/bc.info*
%{_infodir}/dc.info*




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.06.95-3mdv2011.0
+ Revision: 663314
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.06.95-2mdv2011.0
+ Revision: 603756
- rebuild

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.06.95-1mdv2010.1
+ Revision: 462171
- Fix BuildRequires
- Update to new alpha version 1.06.95 (also used by most other distros)
- Remove patches integrated upstream
- Include 2 Fedora/Gentoo patches (fix small memleak, make dc accept
  input which contains wrong symbols of radix in same way like bc)
- SPEC file clean-ups, fix license

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.06-26mdv2010.0
+ Revision: 413155
- rebuild

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 1.06-25mdv2009.1
+ Revision: 344791
- rebuild for new libreadline

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 1.06-24mdv2009.1
+ Revision: 316185
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.06-23mdv2009.0
+ Revision: 220477
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.06-22mdv2008.1
+ Revision: 148915
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.06-21mdv2008.0
+ Revision: 69908
- kill file require on info-install


* Wed Jan 10 2007 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.06-20mdv2007.0
+ Revision: 107132
- cope with new flex

* Tue Sep 19 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.06-19mdv2007.0
- Rebuild

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 1.06-18mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.06-17mdk
- Rebuild

* Fri Aug 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.06-16mdk
- fix rpmlint errors (PreReq)

* Fri Aug 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.06-15mdk
- fix rpmlint errors (PreReq)

* Thu Jan 20 2005 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.06-14mdk
- rebuild for new readline
- fix summary-ended-with-dot

* Sat May 08 2004 Robert Vojta <robert.vojta@mandrake.cz> 1.06-13mdk
- last change reverted - do not change default behavior of these tools!

* Thu May 06 2004 Erwan velu <erwan@mandrakesoft.com> 1.06-12mdk
- Adding alias to run bc in math mode. (1 / 2) will give 0.5 as result and not 0 !

