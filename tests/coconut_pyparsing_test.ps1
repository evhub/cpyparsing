pushd "$HOME/Documents/GitHub/coconut"
make clean
Measure-Command {start-process -wait python ./tests}
popd
