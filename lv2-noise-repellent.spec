%global pname nrepel

%define debug_package %{nil}

Name:           lv2-noise-repellent
Version:        0.1.4
Release:        1%{?dist}
Summary:        An lv2 plug-in for broadband noise reduction
Group:          Applications/Multimedia
License:        GPLv3.0+
URL:            https://github.com/lucianodato/noise-repellent
Source0:        https://github.com/lucianodato/noise-repellent/archive/%{version}.tar.gz

BuildRequires:  lv2-devel
BuildRequires:  fftw-devel
Requires:       lv2
Requires:       fftw-libs

%description
An lv2 plug-in for broadband noise reduction.

%prep
%setup -q -n noise-repellent-%{version}
sed -i -e 's|lib/|%{_lib}/|g' Makefile
sed -i -e 's|-O3|%{optflags}|' Makefile

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
#mkdir -p %{buildroot}/%{_libdir}/lv2
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%doc README.md LICENSE
%{_libdir}/lv2/%{pname}.lv2/*

%changelog
* Fri Jan 12 2018 Nicholas Kudriavtsev <nkudriavtsev@gmail.com>
- Update to 0.1.4 of noise-repelent
* Sun Nov 05 2017 Nicholas Kudriavtsev <nkudriavtsev@gmail.com>
- Initial rpm build
