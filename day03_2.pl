#!/usr/bin/perl

use strict;
use warnings;

my @num1; my @num2; my @num3;
while (<STDIN>) {
    s/\s*(\d+?)\s+?(\d+?)\s+?(\d+)//;
    push @num1, $1;
    push @num2, $2;
    push @num3, $3;
}
push @num1, @num2;
push @num1, @num3;

my $count = 0;
my $x; my $y; my $z;
while (@num1) {
    $x = shift @num1;
    $y = shift @num1;
    $z = shift @num1;
    if ( ($x + $y > $z) && ($x + $z > $y) && ($y + $z > $x)) {
        $count++;
    }
}
print "$count\n"