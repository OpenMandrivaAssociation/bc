Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Name:		bc
Version:	1.07.1
Release:	1
License:	GPLv2+ 
URL:		http://www.gnu.org/software/bc/bc.html
Group:		Sciences/Mathematics
Source0:	http://ftp.gnu.org/gnu/bc/%{name}-%{version}.tar.gz
# Fedora patches
# dc accepts the input which contains wrong symbols of radix in same way like bc (RH bug#151844)
Patch1:		bc-1.06-dc_ibase.patch
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
%apply_patches

%build
%configure \
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
