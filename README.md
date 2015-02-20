# plasmoid-amixer
A simple plasmoid for KDE to send some amixer commands.

![alt tag](https://github.com/neuronalmotion/plasmoid-amixer/raw/develop/img/20150220_first-release.png)

## Features
Currently the plasmoid just display 2 buttons:
* 'Rear' that send the command: amixer sset "Analog Output" "Stereo Headphones"
* 'Front' that send the command: amixer sset "Analog Output" "Stereo Headphones FP"

This configuration allow to switch between "rear output" and the "front output" of a Asus Xonar DGX soundcard.

## How to install
```shell
git clone git@github.com:neuronalmotion/plasmoid-amixer.git
cd plasmoid-amixer
./build.sh
```

The build script will:

1. Create a plasmoid archive (or update it)
2. Try to remove a previous installation of the plasmoid
3. Install the new version of the plasmoid
