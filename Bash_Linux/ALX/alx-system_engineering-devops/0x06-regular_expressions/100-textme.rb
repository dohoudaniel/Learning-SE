#!/usr/bin/env ruby
# A regular expression that outputs specific fields.

puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
