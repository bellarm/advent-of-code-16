#!/usr/bin/perl

use strict;
use warnings;

my $pos = 0;
my $num1; my $num2; my $num3;
while (<STDIN>) {
    s/\s*(\d+?)\s+?(\d+?)\s+?(\d+)//;
    $num1 = $1;
    $num2 = $2;
    $num3 = $3;
    if ( ($num1 + $num2 > $num3) && ($num2 + $num3 > $num1) && ($num1 + $num3 > $num2)) {
        $pos++;
    }
}

print "$pos\n";