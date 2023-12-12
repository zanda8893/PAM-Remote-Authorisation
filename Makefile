PAM_build:
	mkdir -p build
	gcc -g -shared -fPIC -o build/pam_remote.so PAM/main.c

clean:
	rm -r build

install:
	mv build/pam_remote.so /usr/lib/security/pam_remote.so
	cp pam-remote-auth.service /lib/systemd/system/pam-remote-auth.service
	cp remote_auth.conf /etc/remote_auth.conf

	cp PAM_bot.py /usr/sbin/PAM_bot
	python3.11 -m venv /usr/sbin/PAM_bot_lib
	/usr/sbin/PAM_bot_lib/bin/pip3 install -r requirements.txt
	cp PAMlib.py /usr/sbin/PAM_bot_lib/PAMlib.py



	chown root:root /usr/lib/security/pam_remote.so /etc/remote_auth.conf /lib/systemd/system/pam-remote-auth.service /usr/sbin/PAM_bot_lib/PAMlib.py /usr/sbin/PAM_bot
	chmod 700 /usr/lib/security/pam_remote.so /etc/remote_auth.conf /lib/systemd/system/pam-remote-auth.service /usr/sbin/PAM_bot_lib/PAMlib.py /usr/sbin/PAM_bot
	echo "Sucessfully installed"

uninstall:
	rm -r /usr/lib/security/pam_remote.so /lib/systemd/system/pam-remote-auth.service /etc/remote_auth.conf /usr/sbin/PAM_bot /usr/sbin/PAM_bot_lib


