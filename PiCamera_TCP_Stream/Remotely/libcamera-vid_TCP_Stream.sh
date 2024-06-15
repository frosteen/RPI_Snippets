# Add line on crontab -e
# @reboot sh /home/pi/libcamera_TCP_Stream.sh &

# Control RPI Green LED, 0 - OFF and 1 - ON
echo 0 | sudo tee /sys/class/leds/led0/brightness > /dev/null

while true;
do
	echo 1 | sudo tee /sys/class/leds/led0/brightness > /dev/null

	libcamera-vid -t 0 --width 1280 --height 720 --vflip --hflip --framerate 30 -l -o tcp://0.0.0.0:5000 --inline;
	
	echo 0 | sudo tee /sys/class/leds/led0/brightness > /dev/null
done
