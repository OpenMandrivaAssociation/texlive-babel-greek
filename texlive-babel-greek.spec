# revision 31810
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/greek
# catalog-date 2013-10-01 18:30:38 +0200
# catalog-license lppl1.3
# catalog-version 1.7b
Name:		texlive-babel-greek
Version:	1.7b
Release:	1
Summary:	Babel support for documents written in Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/greek
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file provides modes for monotonic (single-diacritic) and
polytonic (multiple-diacritic) modes of writing. Provision is
made for Greek function names in mathematics, and for
classical-era symbols.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-greek/athnum.sty
%{_texmfdistdir}/tex/generic/babel-greek/greek.ldf
%{_texmfdistdir}/tex/generic/babel-greek/grmath.sty
%{_texmfdistdir}/tex/generic/babel-greek/grsymb.sty
%doc %{_texmfdistdir}/doc/generic/babel-greek/README
%doc %{_texmfdistdir}/doc/generic/babel-greek/README.html
%doc %{_texmfdistdir}/doc/generic/babel-greek/athnum.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/greek.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/grmath.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/grsymb.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/test-greek.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/test-greek.tex
%doc %{_texmfdistdir}/doc/generic/babel-greek/test-unicode-greek.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/test-unicode-greek.tex
%doc %{_texmfdistdir}/doc/generic/babel-greek/usage.pdf
%doc %{_texmfdistdir}/doc/generic/babel-greek/usage.tex
#- source
%doc %{_texmfdistdir}/source/generic/babel-greek/athnum.dtx
%doc %{_texmfdistdir}/source/generic/babel-greek/greek.dtx
%doc %{_texmfdistdir}/source/generic/babel-greek/greek.ins
%doc %{_texmfdistdir}/source/generic/babel-greek/grmath.dtx
%doc %{_texmfdistdir}/source/generic/babel-greek/grsymb.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
