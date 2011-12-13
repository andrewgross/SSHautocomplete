What do you do when you want SSH hostname autocompletion on a mac?

1.  Don't google the problem directly, instead assume no one has done it before
2.  Do <b>sudo port install bash-completion</b> for a dependency
3.  Don't realize that it solved your problem.
4.  Do write a parser for an ssh known_hosts file in python for fun and name it parse_hostnames.py
5.  Don't realize you are doing the easy part of the task
6.  Do modify /opt/local/etc/bash_completion.d/ssh and add in ssh_autocomplete.sh as a section
7.  Don't realize that while trouble shooting you rewrote the known_hosts parser in bash
8.  Do pull out the bash known_hosts parser and name it parse_hostnames.sh
9.  Don't get mad when you realize your autocompletion is almost as good as the one in bash-completion
10. Do put your code on Github to attempt to achieve something from all of this


To get SSH hostname completion, all you really need to do is <b>sudo port install bash-completion</b> and add this to the end of your ~/.profile

<code>
if [ -f /opt/local/etc/bash_completion ]; then
   . /opt/local/etc/bash_completion
fi
</code>

Other than that is just inserting the text of ssh_autocomplete.sh, placing the parsing scripts in ~/.ssh and picking which parsing script to use.

A good learning experience, not quite functional because it will attempt to use this completion for all options in scp/ssh. It would really require rewriting the _ssh function and adding this as a special case.