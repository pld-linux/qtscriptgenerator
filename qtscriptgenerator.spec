Summary:	QtScript Qt Bindings
Name:		qtscriptgenerator
Version:	0.1.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://qtscriptgenerator.googlecode.com/files/%{name}-src-%{version}.tar.gz
# Source0-md5:	ca4046ad4bda36cd4e21649d4b98886d
Patch0:		%{name}-qthreadpool.patch
Patch1:		%{name}-no_phonon.patch
URL:		http://code.google.com/p/qtscriptgenerator/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Script Generator is a tool that generates Qt bindings for Qt
Script.

%package -n qtscriptbindings
Summary:	Qt bindings for Qt Script
Group:		Libraries
Requires:	qt4 >= %{qt_ver}

%description -n qtscriptbindings
Binndings providing access to substantial portions of the Qt API from
within Qt Script.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p0
%patch1 -p1

%build
export QTDIR="%{_libdir}/qt4"
export INCLUDE="%{_includedir}/qt4"
cd generator
qmake-qt4
%{__make}
./generator
cd ../qtbindings
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_bindir}
# usually you have to install the program manually

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%{_bindir}/generator

%files -n qtscriptbindings
%defattr(644,root,root,755)
%doc README README.qsexec doc/ examples/
%attr(755,root,root) %{_bindir}/qsexec
#%{_libdir}/script/libqtscript*
