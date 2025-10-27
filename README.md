# HDMI/DP keepalive for linux


Simulates activity on the HDMI/DP output to prevent the TV from switching sources.
Compatible with multiple displays, completely invisible.

Remember to install tk:
* On Arch: 
```bash
"sudo pacman -Sy tk"
``` 
* On Debian: 
```bash
apt install python3-tk tk tk-dev libtcl8.6 libtk8.6 -y
```
* Create the venv
* add screeninfo python module:
```bash
pip install screeninfo
```
