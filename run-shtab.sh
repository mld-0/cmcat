
path_completions="/usr/local/share/zsh/site-functions"

if [ -e "$path_completions/_snek" ]; then
	rm -f "$path_completions/_snek"
fi

#shtab --shell=zsh -u snek.get_main_parser | sudo tee -a "$path_completions/_snek"
#shtab --shell=zsh -u cute_snek.get_main_parser | sudo tee -a "$path_completions/_snek"

#	complete.sh is taken from <print() in script, now disabled> (this completion file is invalid)
cat complete.sh | sudo tee "$path_completions/_snek" > /dev/null

