# -*- encoding: utf-8 -*-
# stub: al_folio_core 1.0.15 ruby lib

Gem::Specification.new do |s|
  s.name = "al_folio_core".freeze
  s.version = "1.0.15".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "allowed_push_host" => "https://rubygems.org", "homepage_uri" => "https://github.com/al-org-dev/al-folio-core", "source_code_uri" => "https://github.com/al-org-dev/al-folio-core" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["al-folio maintainers".freeze]
  s.date = "2026-08-03"
  s.description = "Provides al-folio core runtime hooks, version contract checks, and migration warnings.".freeze
  s.email = ["maintainers@al-folio.dev".freeze]
  s.homepage = "https://github.com/al-org-dev/al-folio-core".freeze
  s.licenses = ["MIT".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.7".freeze)
  s.rubygems_version = "3.5.22".freeze
  s.summary = "Core runtime plugin for al-folio v1.x".freeze

  s.installed_by_version = "3.5.16".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_runtime_dependency(%q<jekyll>.freeze, [">= 3.9".freeze, "< 5.0".freeze])
  s.add_runtime_dependency(%q<liquid>.freeze, [">= 4.0".freeze, "< 6.0".freeze])
  s.add_development_dependency(%q<bundler>.freeze, [">= 2.0".freeze, "< 5.0".freeze])
  s.add_development_dependency(%q<rake>.freeze, ["~> 13.0".freeze])
end
