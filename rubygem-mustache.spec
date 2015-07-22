#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-mustache
Version  : 1.0.2
Release  : 1
URL      : https://rubygems.org/downloads/mustache-1.0.2.gem
Source0  : https://rubygems.org/downloads/mustache-1.0.2.gem
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
%setup -q -D -T -n mustache-1.0.2
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
mustache-1.0.2.gem

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
/usr/lib64/ruby/gems/2.2.0/cache/mustache-1.0.2.gem
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/%5b%5d%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/%5b%5d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/cdesc-Context.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/current-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/escapeHTML-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/fetch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/find-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/find_in_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/has_key%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/mustache_in_stack-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/partial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/pop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/push-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/template_for_partial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Context/to_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/ContextMiss/cdesc-ContextMiss.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/cdesc-Generator.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/compile%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/compile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/ev-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/on_etag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/on_fetch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/on_inverted_section-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/on_partial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/on_section-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/on_utag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Generator/str-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%21%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%23%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%2f%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%3c%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%3d%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%3e%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/%27scan_tag_%5e%27-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/SyntaxError/cdesc-SyntaxError.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/SyntaxError/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/SyntaxError/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/add_type-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/cdesc-Parser.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/compile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/content_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/ctag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/dispatch_based_on_type-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/find_closing_tag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/offset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/otag-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/position-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/regexp-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_block-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_close-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_comment-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_delimiter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_inverted-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_open_partial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tag_unescaped-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/scan_until_exclusive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Parser/valid_types-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/cdesc-Template.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/compile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/partials-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/recursor-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/sections-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/source-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/tags-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Template/tokens-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Utils/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Utils/String/classify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Utils/String/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Utils/String/underscore-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/Utils/cdesc-Utils.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/cdesc-Mustache.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/classify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/compiled%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/compiled%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/const_from_file-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/context-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/escapeHTML-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/inheritable_config_for-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/partial-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/partial-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/path%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/raise_on_context_miss%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/raise_on_context_miss%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/raise_on_context_miss%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/raise_on_context_miss%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/render-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/render_file-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/render_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/rescued_const_get-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_extension%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_extension%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_extension-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_extension-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_file%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_file%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_file-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_name%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_name%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_name-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_path%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_path%3d-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/template_path-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/templateify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/templateify-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/underscore-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/view_class-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/view_namespace%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/view_namespace-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/view_path%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/Mustache/view_path-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/mustache-1.0.2/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/README.md
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/bin/mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/context.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/context_miss.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/enumerable.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/parser.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/settings.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/template.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/utils.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/lib/mustache/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/man/mustache.1
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/man/mustache.1.html
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/man/mustache.1.ron
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/man/mustache.5
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/man/mustache.5.html
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/man/mustache.5.ron
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/autoloading_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/comments.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/comments.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/complex_view.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/complex_view.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/crazy_recursive.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/crazy_recursive.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/delimiters.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/delimiters.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/dot_notation.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/dot_notation.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/double_section.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/double_section.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/escaped.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/escaped.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/inner_partial.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/inner_partial.txt
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/inverted_section.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/inverted_section.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/lambda.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/lambda.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/liberal.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/liberal.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/method_missing.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/namespaced.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/namespaced.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/nested_objects.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/nested_objects.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/node.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/partial_with_module.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/partial_with_module.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/passenger.conf
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/passenger.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/recursive.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/recursive.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/simple.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/simple.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/simply_complicated.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/template_partial.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/template_partial.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/template_partial.txt
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/unescaped.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/unescaped.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/utf8.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/fixtures/utf8_partial.mustache
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/mustache_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/parser_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/partial_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/spec_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/mustache-1.0.2/test/template_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/mustache-1.0.2.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/mustache
