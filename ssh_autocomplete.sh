#ssh-known-hosts completion
#
_ssh_known_hosts()
{
   local cur prev opts
   COMPREPLY=()
   cur="${COMP_WORDS[COMP_CWORD]}"
   prev="${COMP_WORDS[COMP_CWORD-1]}"

   if [ -n "$(echo ${cur} | grep '@')"  ] ; then
      root_word=$(echo ${cur} |awk -F@ '{print $1}')
      partial=$(echo ${cur} | tr -d ${root_word}@)
      opts="$(cat ~/.ssh/known_hosts | awk '{print $1}' | egrep -v '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$' | awk -F\, '{print $1}' | uniq | sort)"
      tmp=""
      for opt in ${opts}
      do
              tmp="${tmp} ${root_word}@${opt}"
      done
      opts=${tmp}
      COMPREPLY=( $(compgen -W "${opts}" ${cur}) )
       return 0
   fi
}
complete -F _ssh_known_hosts ssh
complete -F _ssh_known_hosts scp