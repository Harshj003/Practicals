#!usr/bin/perl
use strict;
use warnings;
print "no","\n";
my $n = <STDIN>;
my $count=2;
my $j=2;
my $zero_rem = 0;
my $rem = $n % $j;
for (my $count=2; $count<=$n; $count++) {
  $zero_rem = 0;
  for (my $j=2;$j<$count;$j++){
    $rem = $count % $j;
    if ($rem == 0){
      $zero_rem = 1;
      last;
    }
  }
  if(!$zero_rem){
    print "$count is a prime\n";
  }
}
