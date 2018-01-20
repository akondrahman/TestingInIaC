=begin
This script extarcts AST from
rspec tests for Puppet
=end
require 'rubocop'  ### need to import module 'RubCop'

#code = '!something.empty?'
## now read file into string and let RuboCop parse it
code_content = File.read('/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/cisco-puppet-openstack-repo/spec/classes/openstack_compute_spec.rb')
source = RuboCop::ProcessedSource.new(code_content, RUBY_VERSION.to_f)
node = source.ast
puts node  ### to see what AST it gives
