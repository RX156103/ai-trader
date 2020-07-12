cp config/config.json.sample config/config.json
sudo chmod +x docker_ubuntu_install.sh && sudo ./docker_ubuntu_install.sh
sudo docker run -d --rm --mount src=`pwd`/config,target=/breakout-trader/config,type=bind skilfulll1/breakout-trader:latest