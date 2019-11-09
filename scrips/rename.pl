use strict;
use warnings;

my $count=1;
open IN,'<',"uniprot-yeast.fasta" or die "IN,$!\n";                      #assembly.fa is your own inputfile
open OUT,'>',"assembly22.fa" or die "OUT,$!\n";        #assembly22.fa is the outputfile you want to name
my @lines = <IN>;
foreach my $line(@lines){
   chomp($line);
   if($line=~/^>/){
       print OUT">$count\n";
      $count++;
    }else{
       print OUT"$line\n";
    }
}
