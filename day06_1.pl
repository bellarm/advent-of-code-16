#!/usr/bin/perl

use strict;
use warnings;

my %count;
while (<STDIN>) {
    chomp;
    my @word = split(//, $_);
    my $pos = 0;
    foreach my $letter (@word) {
        $count{$pos++}{$letter}++;
    }
}

foreach my $x (sort keys %count) {
    foreach my $y (sort { $count{$x}{$b} <=> $count{$x}{$a} } keys($count{$x})) {
        print "$x $y = $count{$x}{$y}\n";
        last;
    }
}