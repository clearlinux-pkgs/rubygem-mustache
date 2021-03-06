#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-mustache
Version  : 1.0.3
Release  : 5
URL      : https://rubygems.org/downloads/mustache-1.0.3.gem
Source0  : https://rubygems.org/downloads/mustache-1.0.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-mustache-bin
BuildRequires : ruby
BuildRequires : rubygem-benchmark-ips
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-ruby-prof

%description
# Mustache
[![Gem Version](https://badge.fury.io/rb/mustache.svg)](http://badge.fury.io/rb/mustache)
[![Build Status](https://travis-ci.org/mustache/mustache.svg?branch=master)](https://travis-ci.org/mustache/mustache)

%package bin
Summary: bin components for the rubygem-mustache package.
Group: Binaries

%description bin
bin components for the rubygem-mustache package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n mustache-1.0.3
gem spec %{SOURCE0} -l --ruby > rubygem-mustache.gemspec

%build
gem build rubygem-mustache.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
mustache-1.0.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/mustache-1.0.3.gem
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/README.md
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/bin/mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/context.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/context_miss.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/enumerable.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/settings.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/template.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/lib/mustache/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/man/mustache.1
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/man/mustache.1.html
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/man/mustache.1.ron
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/man/mustache.5
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/man/mustache.5.html
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/man/mustache.5.ron
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/autoloading_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/comments.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/comments.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/complex_view.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/complex_view.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/crazy_recursive.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/crazy_recursive.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/delimiters.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/delimiters.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/dot_notation.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/dot_notation.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/double_section.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/double_section.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/escaped.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/escaped.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/inner_partial.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/inner_partial.txt
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/inverted_section.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/inverted_section.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/lambda.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/lambda.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/liberal.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/liberal.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/method_missing.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/namespaced.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/namespaced.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/nested_objects.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/nested_objects.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/node.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/partial_with_module.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/partial_with_module.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/passenger.conf
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/passenger.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/recursive.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/recursive.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/simple.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/simple.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/simply_complicated.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/template_partial.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/template_partial.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/template_partial.txt
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/unescaped.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/unescaped.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/utf8.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/fixtures/utf8_partial.mustache
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/mustache_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/parser_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/partial_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/spec_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/mustache-1.0.3/test/template_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/mustache-1.0.3.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/mustache
