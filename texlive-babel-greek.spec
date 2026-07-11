%global tl_name babel-greek
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.15
Release:	%{tl_revision}.1
Summary:	Babel support for the Greek language and script
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/greek
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-greek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides comprehensive support for the Greek language and
script via the Babel system. Document authors can select between the
monotonic (single-diacritic), polytonic (multiple-diacritic), and
ancient orthography of the Greek language. Included are the packages
grmath for Greek function names in mathematics, and athnum for Attic
numerals.

