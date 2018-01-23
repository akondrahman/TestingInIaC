=begin
This script extracts details from the Puppet Forge module
using the forge gem API
isntall the gem first
=end
require 'puppet_forge'
mod_name = 'puppetlabs-apache'
my_module = PuppetForge::Module.find(mod_name)
# dloads = my_module.downloads
# puts "Downloads: #{dloads}"
curr_rel= my_module.current_release
rel_ver = curr_rel.version
puts "Curent release: #{rel_ver}"
my_mod_curr_rel = PuppetForge::Release.find(mod_name+ "-" + rel_ver)
puts my_mod_curr_rel.downloads
