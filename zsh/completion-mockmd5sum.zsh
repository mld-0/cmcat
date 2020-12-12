#	first line must be compdef statement, with name of command to be completed
#compdef mockmd5sum

#	LINK: http://bewatermyfriend.org/p/2012/003/
#	LINK: http://zsh.sourceforge.net/Doc/Release/Completion-System.html
#	Book: Learning Shell Scripting with Zsh (Ch5, Completion)

#	_arguments, (function), handles option arguments to be formatted and displayed (when following unix convention)
#	'--' is the end parsing of option delimiter
#	-S, do not complete options after '--' end parsing delimitor

#	pattern of argument entries:
#	(optional exclusion list), {options}, [help text]
#		exclusion list: If given items appear (elsewhere) in the (current) command line, do not show them as completions
#			eg: '(-L -P)-H[with -R, follow symlinks on the command line]' -> hide -L and -P if -H is used
#		options: {} braces are excluded if there is only one option?
#	'*:files:_files' standard helper function for completing filenames ('_files' uses helper function '_path_files')
#	_call_program -> additional help function, execute system commands

_arguments -S \
  '(-b --binary)'{-b,--binary}'[read in binary mode]' \
  '(-c --check)'{-c,--check}'[read MD5 sums from the FILEs and check them]' \
  '(-t --text)'{-t,--text}'[read in text mode]' \
  '--status[no output, status code shows success]' \
  '(-w --warn)'{-w,--warn}'[warn about improperly formatted checksum lines]' \
  '--help[display help and exit]' \
  '--version[output version information and exit]' \
  '*:files:_files'

#>% 	echo $functions[_mockmd5sum]
#>>		_arguments -S '(-b --binary)'{-b,--binary}'[read in binary mode]' '(-c --check)'{-c,--check}'[read MD5 sums from the FILEs and check them]' '(-t --text)'{-t,--text}'[read in text mode]' '--status[no output, status code shows success]' '(-w --warn)'{-w,--warn}'[warn about improperly formatted checksum lines]' '--help[display help and exit]' '--version[output version information and exit]' '*:files:_files'

#>%		mockmd5sum<C-x>, h 		dump zsh completion content
#>>		tags in context :completion::complete:mockmd5sum::
#>>		    argument-rest options  (_arguments _mockmd5sum)
#>>		tags in context :completion::complete:mockmd5sum:argument-rest:
#>>		    globbed-files  (_files _arguments _mockmd5sum)


#	Example, 'elm'
#>%		#compdef elm
#>%		
#>%		_arguments -s \
#>%		  '::recipient:_email_addresses' \
#>%		  '-a[use the arrow pointer regardless]' \
#>%		  '-A+[attach file]:file attachment:_files' \
#>%		  '-c[check the given aliases only]:*:alias' \
#>%		  '-d+[set debug level]:debug level' \
#>%		  '-f+[specify mailbox to load]:mailbox: _mailboxes' \
#>%		  '-h[display help]' \
#>%		  '-i+[specify file to include in message]:include file:_files' \
#>%		  '-m[turn off menu, using more of the screen]' \
#>%		  '-s+[specify a subject]:subject:' \
#>%		  "-t[don't use termcap/terminfo ti/te entries]" \
#>%		  '-V[enable sendmail voyeur mode]' \
#>%		  '-v[display elm version]' \
#>%		  '-w[write .elm/elmrc]' \
#>%		  '-z[start only if new messages]'

#	How completion situation is handeled
#>%		elm -A <tab>
#	The shell starts and somewhere in your `.zshrc' file you are calling "autoload -Uz compinit; compinit". Now, compsys is online.
#	While compinit is running it will find the `_elm' file in one directory of `$fpath'.
#	Compinit will read the first like of that file, find out that it's a completion for a command called "elm" and make a note of that in a mapping for later.
#	Then compinit will call `autoload' for the "_elm" file, so its code is loaded from the file when it is referenced for the first time.
#	At the prompt, you typed "elm -A " and pressed the tab key, which will set the completion system in motion.
#	Compsys recognises, that for the current cursor position the word in command position is "elm".
#	It'll look up which completion function is in charge for that command in the mapping it made during startup. It'll find that that's "_elm".
#	That function gets called and (when it is run for the first time) zsh automatically loads its code from the "_elm" file in `$fpath'.
#	The `_arguments' function analyses the situation and figures out, that it needs to handle an argument to the "-A" option of the command, which it delegates to the `_files' function - as specified in the option's optspec.
#	The result is that you are being presented with a list of files, which is useful for elm's "-A" option.

