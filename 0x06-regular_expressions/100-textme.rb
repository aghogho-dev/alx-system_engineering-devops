#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([+A-z0-9]+)\] \[to:([+0-9]+)\] \[flags:([-:01]+)\]/).join(",")
