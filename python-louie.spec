%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Dispatches signals between Python objects in a wide variety of contexts
Name: python-louie
Version: 1.1
Release: 7%{?dist}
License: BSD
Group: Development/Languages
URL: http://11craft.github.com/louie/
Source: http://cheeseshop.python.org/packages/source/L/Louie/Louie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-setuptools
# From the egg requires.txt
Requires: python-nose >= 0.8.3
BuildRequires: python-devel
# Must have setuptools to build the package
# The build portions moved to a subpackage in F-8
%if 0%{?fedora} >= 8 || 0%{?rhel} >= 6
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif
BuildArch: noarch

%description
Louie provides Python programmers with a straightforward way to dispatch
signals between objects in a wide variety of contexts. It is based on
PyDispatcher, which in turn was based on a highly-rated recipe in the
Python Cookbook.


%prep
%setup -q -n Louie-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

# Remove empty files
%{__rm} %{buildroot}/%{python_sitelib}/Louie-*.egg-info/not-zip-safe
%{__rm} %{buildroot}/%{python_sitelib}/louie/test/fixture.py

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc doc/*.txt
%{python_sitelib}/Louie-*.egg-info/
%{python_sitelib}/louie/


%changelog
* Wed May 26 2010 Bastien Nocera <bnocera@redhat.com> 1.1-7
- Remove empty files, fix project URL
Related: rhbz#595761

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-6.1
- Fix conditional for RHEL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Matthias Saou <http://freshrpms.net/> 1.1-4
- Add python-nose >= 0.8.3 requirement taken from the egg file.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-3
- Rebuild for Python 2.6

* Tue Aug 28 2007 Matthias Saou <http://freshrpms.net/> 1.1-2
- Update python-setuptools build requirement to new python-setuptools-devel.

* Fri Feb  9 2007 Matthias Saou <http://freshrpms.net/> 1.1-1
- Initial RPM release.

