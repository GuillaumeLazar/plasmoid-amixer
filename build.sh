#/bin/bash

cd src
zip -r ../nm-plasmoid-amixer.zip .
cd ..

plasmapkg -r nm-plasmoid-amixer
sleep 1
plasmapkg -i nm-plasmoid-amixer.zip 

