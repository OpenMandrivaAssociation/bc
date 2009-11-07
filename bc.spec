Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Name:		bc
Version:	1.06.95
Release:	%mkrel 1
License:	GPLv2+ 
URL:		http://www.gnu.org/software/bc/bc.html
Group:		Sciences/Mathematics
Source:		ftp://ftp.gnu.org/gnu/bc/%{name}-%{version}.tar.bz2
# Fedora patches
# dc accepts the input which contains wrong symbols of radix in same way like bc (RH bug#151844)
Patch1: bc-1.06-dc_ibase.patch
# fix small memory leak (gentoo patch)
Patch2: bc-1.06.95-memleak.patch
BuildRequires:	flex ncurses-devel readline-devel
BuildRequires:	texinfo
Requires(post):  info-install grep
Requires(preun):info-install grep
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%configure2_5x --with-readline
%make

%install
rm -rf %{buildroot}
%{makeinstall}

%clean
rm -rf %{buildroot}

%post
%_install_info bc.info
%_install_info dc.info

%preun
%_remove_install_info bc.info
%_remove_install_info dc.info

%files
%defattr(-,root,root)
%doc FAQ AUTHORS NEWS README
%{_bindir}/bc
%{_bindir}/dc
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%{_infodir}/bc.info*
%{_infodir}/dc.info*


