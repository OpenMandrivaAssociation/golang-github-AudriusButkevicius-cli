# https://github.com/AudriusButkevicius/cli
%global goipath github.com/AudriusButkevicius/cli
%global commit  7f561c78b5a4aad858d9fd550c92b5da6d55efbb
%global date    20140727

%gometa

Name:           golang-github-AudriusButkevicius-cli
Version:        1.0.0
Release:        8%{?dist}
Summary:        Small library for building CLI apps in Go
License:        MIT

URL:            %{gourl}
Source0:        %{gosource}

# Upstream pull request to fix failing compilation of tests
# https://github.com/AudriusButkevicius/cli/pull/1
Patch0:         00-fix-go-111-unused-errors.patch

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-8.20140727git7f561c7
- Use forgeautosetup instead of gosetup.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-7.20140727git7f561c7
- Update to use spec 3.0.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-6.20140727.git7f561c7
- Include patch to fix building tests with go 1.11.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1.20140727.git7f561c7
- First package for Fedora

