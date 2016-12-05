#!/usr/bin/perl

use strict;
use warnings;

our @keys = (['0', '0', '1', '0', '0'], ['0','2','3','4','0'], ['5','6','7','8','9'], ['0','A','B','C','0'], ['0','0','D','0','0']);

sub get_pos {
    my ($step, $row, $col) = @_;
    our @keys;
    if ($step eq 'R'){
        $col++ if ($col+1 != 5 && ord($keys[$row][$col+1]) != ord('0'));
    } elsif ($step eq 'L') {
        $col-- if ($col-1 != -1 && ord($keys[$row][$col-1]) != ord('0'));
    } elsif ($step eq 'U') {
        $row-- if ($row-1 != -1 && ord($keys[$row-1][$col]) != ord('0'));
    } elsif ($step eq 'D') {
        $row++ if ($row+1 != 5 && ord($keys[$row+1][$col]) != ord('0'));
    }
    return ($row, $col);
}

my @steps;
my $i = 0;
while (<STDIN>) {
    chomp;
    $steps[$i++] = $_;
}

my $row = 2;
my $col = 0;
foreach my $step (@steps) {
    my @step = split(//, $step);
    foreach my $move (@step) {
        ($row, $col) = get_pos($move, $row, $col);
        # print "move: $move moving to $keys[$row][$col]\n";
    }
    print "\t$keys[$row][$col]\n";
}
