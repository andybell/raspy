# User notes for Raspbery pi 

## Secure copy

Use ```scp user@remoteip:file.txt /some/local/dir``` to transer from remote to local

Use ```scp file.txt user@remoteip:~/Downloads``` to transer file from local to remote


See: http://www.hypexr.org/linux_scp_help.php

## Mount USB drive

### mount 

```sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/usb_name```


### unmount 

```sudo umount /mnt/usb_name```

Important: it's ```umount``` without the "n"

See: http://elinux.org/RPi_Adding_USB_Drives


## Static IP's



See: http://elinux.org/Configuring_a_Static_IP_address_on_your_Raspberry_Pi
or see: http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/