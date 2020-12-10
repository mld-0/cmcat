[ -z $mld_loaded_exports ] && source "$HOME/._exports.sh"
[ -z $mld_loaded_bins ] && source "$HOME/._bins.sh"

#	valid command, but does not give us 'snek' as a command, since where the (executable representation) of the package ends up is not in $PATH
python setup.py develop

#	To make 'snek' work as a standalone command, add to PATH:
#>%		$( dirname $( pyenv which python ) )

