# plasmoid-amixer
A simple plasmoid for KDE to send some amixer commands.

![alt tag](https://github.com/neuronalmotion/plasmoid-amixer/raw/develop/img/20150222_with-images.png)

## Features
Currently the plasmoid just display a button with 2 actions:
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

## GFX Credits
License: Creative Commons 
* http://icons4android.com/
* http://www.google.com/design/
