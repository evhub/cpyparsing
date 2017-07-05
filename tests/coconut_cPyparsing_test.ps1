pushd "$HOME/Documents/GitHub/coconut"
make clean
Measure-Command {start-process -wait powershell "$HOME/Documents/GitHub/cpyparsing/tests/run_coconut_with_cPyparsing.ps1"}
popd
