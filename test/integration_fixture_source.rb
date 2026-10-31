# Isolated pages for integration tests, independent of published demo content.
require 'fileutils'
require 'yaml'

source = File.expand_path('fixture-source', ARGV.fetch(0))
FileUtils.mkdir_p(source)
pages = {
  'index.md' => { 'layout' => 'page', 'title' => 'Integration home', 'permalink' => '/' },
  'giscus.md' => {
    'layout' => 'post', 'title' => 'Giscus fixture', 'giscus_comments' => true,
    'related_posts' => false, 'permalink' => '/blog/2022/giscus-comments/'
  },
  'disqus.md' => {
    'layout' => 'post', 'title' => 'Disqus fixture', 'disqus_comments' => true,
    'related_posts' => false, 'permalink' => '/blog/2015/disqus-comments/'
  },
  'distill.md' => {
    'layout' => 'distill', 'title' => 'Distill fixture', 'giscus_comments' => true,
    'mermaid' => { 'enabled' => true }, 'tikzjax' => true,
    'permalink' => '/blog/2021/distill/'
  },
  'rtl.md' => {
    'layout' => 'post', 'title' => 'RTL fixture', 'lang' => 'fa',
    'related_posts' => false, 'permalink' => '/blog/2022/rtl/'
  },
  'marimo.md' => {
    'layout' => 'post', 'title' => 'Marimo fixture', 'marimo' => true,
    'related_posts' => false, 'permalink' => '/blog/2025/marimo/'
  }
}
pages.each do |filename, front_matter|
  File.write(File.join(source, filename), "#{front_matter.to_yaml}---\n\nIntegration fixture.\n")
end
puts source
