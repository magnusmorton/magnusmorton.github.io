%global pkg rainbow-delimiters
%global pkgname "rainbow-delimiters"

Name:		emacs-%{pkg}
Version:	2.1.5
Release:	1%{?dist}
Summary:	Highlight brackets according to their depth

License:	GPLv3+
URL:		https://github.com/Fanael/rainbow-delimiters
Source0:	https://github.com/Fanael/rainbow-delimiters/archive/%{version}/%{pkg}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	emacs
Requires:	emacs(bin) >= %{_emacs_version}

%description

rainbow-delimiters is a "rainbow parentheses"-like mode which highlights
delimiters such as parentheses, brackets or braces according to their
depth. Each successive level is highlighted in a different color. This makes it
easy to spot matching delimiters, orient yourself in the code, and tell which
statements are at a given depth.

Great care has been taken to make this mode fast. You shouldn't see any change
in scrolling or editing speed when it's on even when working in delimiter-rich
languages like Clojure or Emacs Lisp. It can be used with any language.

You can customize the colors rainbow-delimiters uses. The default colors are
intentionally subtle; they are unobtrusive enough to make the mode worth looking
at even if you usually don't like rainbow parentheses modes. A number of major
color themes such as Zenburn and Solarized have added their own faces for the
mode.

%prep
%setup -q -n %{pkg}-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}
cp -p %{pkg}.el %{pkg}.elc $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}

%check
emacs -Q -batch -l rainbow-delimiters-test.el -f ert-run-tests-batch-and-exit

%files
%{_emacs_sitelispdir}/%{pkg}

%doc README.md

%changelog


* Wed Sep 08 2021 Magnus Morton <magnus@morton.ai> - 2.1.5-1
- Initial spec file

