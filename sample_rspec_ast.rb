=begin
This script extarcts AST from
rspec tests for Puppet
=end
require 'rubocop'  ### need to import module 'RubCop'

## now read file into string and let RuboCop parse it
code_content = File.read('/Users/akond/Documents/AkondOneDrive/OneDrive/CSC712/project-materials/cisco-puppet-openstack-repo/spec/classes/openstack_compute_spec.rb')
source = RuboCop::ProcessedSource.new(code_content, RUBY_VERSION.to_f)
node = source.ast
# puts node  ### to see what AST it gives
=begin
convert AST to str , search the string after that 
=end
node_as_str = node.to_s()
param_matches = node_as_str.scan(/:params/)
puts "Count of parameters: #{param_matches.length}"
it_matches = node_as_str.scan(/:it/)
puts "Count of it clauses: #{it_matches.length}"
should_matches = node_as_str.scan(/:should/)
puts "Count of should clauses: #{should_matches.length}"
