#
# TODO:
# Build without no_phonon.patch (fix qt4.spec)
#
%define		qt_ver	4.5.0

Summary:	QtScript Qt Bindings
Name:		qtscriptgenerator
Version:	0.1.0
Release:	1
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
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtScriptTools-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtUiTools-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	QtXmlPatterns-devel
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

for dir in generator qtbindings tools/qsexec/src; do
	cd $dir
	qmake-qt4
	%{__make}
	test "$dir" == "generator" && ./generator
	cd -
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/qt4/plugins/script/,%{_libdir}/qt4/bin}

# install doesn't do symlinks
cp -a plugins/script/libqtscript* \
  $RPM_BUILD_ROOT%{_libdir}/qt4/plugins/script/

install tools/qsexec/README.TXT README.qsexec
install tools/qsexec/qsexec $RPM_BUILD_ROOT%{_bindir}/qsexec
install generator/generator $RPM_BUILD_ROOT%{_libdir}/qt4/bin/generator

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/qt4/bin/generator

%files -n qtscriptbindings
%defattr(644,root,root,755)
%doc README README.qsexec doc/ examples/
%attr(755,root,root) %{_bindir}/qsexec
%{_libdir}/qt4/plugins/script/libqtscript*
