
[ -z $mld_loaded_exports ] && source "$HOME/._exports.sh"
[ -z $mld_loaded_bins ] && source "$HOME/._bins.sh"

#	See:
#	LINK: https://amir.rachum.com/blog/2017/07/28/python-entry-points/

#	When running with pyenv python, add to PATH the directory (see below) where the executibles will be placed, i.e:
#>%		PATH=$PATH:$( dirname $( pyenv which python ) )

cd snek
python setup.py develop 
cd ..

cd cute_snek
python setup.py develop 
cd ..

