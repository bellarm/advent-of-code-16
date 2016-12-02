#!/usr/bin/perl

use strict;
use warnings;

sub get_pos {
    my ($step, $pos) = @_;
    if ($step eq 'R'){
        $pos++ if ($pos % 3 != 0);
    } elsif ($step eq 'L') {
        $pos-- if ($pos % 3 != 1);
    } elsif ($step eq 'U') {
        $pos -= 3 if ($pos - 3 > 0);
    } elsif ($step eq 'D') {
        $pos += 3 if ($pos + 3 < 10);   
    }
    return $pos;
}

my @steps;
my $i = 0;
while (<STDIN>) {
    chomp;
    $steps[$i++] = $_;
}

my $pos = 5;
foreach my $step (@steps) {
    my @step = split(//, $step);
    foreach my $move (@step) {
        $pos = get_pos($move, $pos);
    }
    print "$pos";
}