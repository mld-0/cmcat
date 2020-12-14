
path_file="$1"
colnum="$2"

perl -lane "print \$F[$colnum] if ! \$seen{\$F[$colnum]}++" "$path_file"
