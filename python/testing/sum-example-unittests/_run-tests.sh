#!/usr/bin/env zsh
# 	VIM SETTINGS: {{{3
# 	VIM: let g:mldvp_filecmd_open_tagbar=0 g:mldvp_filecmd_NavHeadings="" g:mldvp_filecmd_NavSubHeadings="" g:mldvp_filecmd_NavDTS=0 g:mldvp_filecmd_vimgpgSave_gotoRecent=0
# 	vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
# 	vim: set foldlevel=2 foldcolumn=3: 
# 	}}}1
[ -z $mld_loaded_exports ] && source "$HOME/._exports.sh"
[ -z $mld_loaded_bins ] && source "$HOME/._bins.sh"

#	For tests to function, working directory when calling script must be directory containing script, i.e: project top-level directory

#	Tests may be run with
#>%		python -m tests.test
#>%		python -m unittest discover -s tests

python -m unittest -v tests.test

#	To run tests from arbitrary directory, specify location of project parent directory where tests should be performed
#>%		python -m unittest discover -s tests -t $path_src


