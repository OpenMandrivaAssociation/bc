%define name	bc
%define version	1.06
%define release %mkrel 20

Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://www.gnu.org/software/bc/bc.html
Group:		Sciences/Mathematics
Source:		ftp://ftp.gnu.org/gnu/bc/%{name}-%{version}.tar.bz2
Patch0:		bc-1.06-readline42.patch
Patch1:		bc-1.06-fixes.patch
Patch2:		bc-1.06-info-dir-entry.patch
Patch3:		bc-1.06-flex.patch
BuildRequires:	flex ncurses-devel readline-devel
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
%patch0 -p1 -b .readline42
%patch1 -p1 -b .fixes
%patch2 -p1 -b .info-dir-entry
%patch3 -p1 -b .flex

# don't bother with autoconf et al.
touch aclocal.m4
find . -name Makefile.in | xargs touch

%build
%configure --with-readline
make LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall}
mkdir -p $RPM_BUILD_ROOT/etc/profile.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info bc.info
%_install_info dc.info

%preun
%_remove_install_info bc.info
%_remove_install_info dc.info

%files
%defattr(-,root,root)
%doc COPYING COPYING.LIB FAQ AUTHORS NEWS README
%{_bindir}/bc
%{_bindir}/dc
%{_mandir}/man1/bc.1*
%{_mandir}/man1/dc.1*
%{_infodir}/bc.info*
%{_infodir}/dc.info*


