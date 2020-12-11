
[ -z $mld_loaded_exports ] && source "$HOME/._exports.sh"
[ -z $mld_loaded_bins ] && source "$HOME/._bins.sh"

set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

#	To use resulting 'greeter' as executable, need to add $( dirname $( pyenv which python ) ) to PATH

#	Install greeter
python setup.py develop

#	Use greeter to generate completions, and write to applicable file
path_completions="/usr/local/share/zsh/site-functions"
greeter -z | tee "$path_completions/_greeter" > /dev/null

