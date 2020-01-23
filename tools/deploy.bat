pushd %~dp0..
python tools\deploy.py --target %AppData%\FactorioMETF\mods --target %AppData%\Factorio\mods
popd