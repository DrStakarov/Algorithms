#!/usr/bin/env ruby

def sayhello(name, number)
    puts "Hello #{name.to_s} #{number.to_s}!"
end

name = ARGV[0]
10.times { |num| sayhello(name, num) }