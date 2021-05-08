Summary:	lzip file decompressor
Summary(pl.UTF-8):	Dekompresor plików w formacie lzip
Name:		lunzip
Version:	1.12
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/lunzip/%{name}-%{version}.tar.lz
# Source0-md5:	932c136414ab44e758ca3c03bc49fa8c
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lunzip is a decompressor for lzip files. It is written in C and its
small size makes it well suited for embedded devices or software
installers that need to decompress files but do not need compression
capabilities. Lunzip is fully compatible with lzip-1.4 or newer.

%description -l pl.UTF-8
Lunzip to dekompresor plików w formacie lzip. Jest napisany w C, a
mały rozmiar pozwala używać go na systemach wbudowanych lub w
instalatorach potrzebujących jedynie zdekompresować pliki, bez
potrzeby kompresji. Lunzip jest w pełni kompatybilny z lzipem 1.4 i
nowszymi wersjami.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/lunzip
%{_mandir}/man1/lunzip.1*
