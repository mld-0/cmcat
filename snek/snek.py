
#   LINK: https://amir.rachum.com/blog/2017/07/28/python-entry-points/

"""Print an ASCII Snek.

Usage:
    snek [--type=TYPE]
    
"""
import docopt
import argopt, shtab
import pkg_resources

normal_snek = """\
    --..,_                     _,.--.
       `'.'.                .'`__ o  `;__.
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""

fancy_snek = """\
                          _,..,,,_
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
"""

def get_sneks():
    sneks = {}
    for entry_point in pkg_resources.iter_entry_points('snek_types'):
        sneks[entry_point.name] = entry_point.load()
    return sneks


def main():
    #args = docopt.docopt(__doc__)
    #snek_type = args['--type'] or 'normal'
    args = parser.parse_args()
    snek_type = args.type or 'normal'
    print(get_sneks()[snek_type])

parser = argopt.argopt(__doc__)
#shtab.add_argument_to(parser, ["-s", "--print-completion"])
#print(shtab.complete(parser, shell="zsh"))
    
if __name__ == '__main__':
    main()
