%global tl_name domaincoloring
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.05
Release:	%{tl_revision}.1
Summary:	Draw colored represenations of complex functions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/domaincoloring
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/domaincoloring.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/domaincoloring.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Domain coloring is a technique to visualize complex functions by
assigning a color to each point of the complex plane z=x+iy. This
package calculates with the help of Lua any complex function to
visualize its behaviour. The value of the complex function(z) can be
described by radius and angle which can be two values of the hsv-color
model, which then defines the color of each point in the complex plane
z=x+iy.

