#!/usr/bin/env ruby

def sayhello(name)
    puts "hello #{name.to_s}"
end

name = ARGV[0]
sayhello(name)