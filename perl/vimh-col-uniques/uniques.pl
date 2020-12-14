#	VIM SETTINGS: {{{3
#	VIM: let g:mldvp_filecmd_open_tagbar=0 g:mldvp_filecmd_NavHeadings="" g:mldvp_filecmd_NavSubHeadings="" g:mldvp_filecmd_NavDTS=0 g:mldvp_filecmd_vimgpgSave_gotoRecent=0
#	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#	vim: set foldlevel=2 foldcolumn=3: 
#	}}}1
use strict;
use warnings; 
my $filename = $ARGV[0];
my $colnum = $ARGV[1];
open(FILE, $filename) or die "Could not open file '$filename' $!";
my %seen;
while (<FILE>)
{
    chomp;
    my $line = $_;
    my @elements = split (" ", $line);
    my $row_name = $elements[$colnum];
    print $row_name . "\n" if ! $seen{$row_name}++;
}
close FILE;

