Uploads screenshots directly to your backend and displays URL.

## Installation
### Via github.com

The latest development version can be installed manually with these commands:

```sh
git clone https://github.com/PACordonnier/gnome-shell-upload-screenshot.git
cd gnome-shell-upload-screenshot
make install
```

Then use gnome-tweak-tool.

##Backend
With the backend, my goal was to mock the imgur API, in order to keep the plugin nearly unmodified.
The backend receive the image under the name 'image'.
Once uploaded, the JSON response contains a object 'body' which contains the url under the name of 'link'

```JSON
{
	"data": {
		"link": "www.myserver.com/myimage.png"
	}
}
```
This URL is then displayed in the notification

A very simple server is provided in the folder server/, using the Python framework Flask. You should see the documentation in order to get it working.

## Contributors

* Andrey Sitnik - https://github.com/ai
* Geoff Saulmon - https://github.com/gsaulmon
* Jacob Mischka - https://github.com/jacobmischka
* Kate Adams - https://github.com/KateAdams
* Maxim Kraev - https://github.com/MaximKraev
* papertoilet - https://github.com/papertoilet
* Sigmund Vestergaard - https://github.com/sigmundv
* Paul-Adrien Cordonnier - https://github.com/PACordonnier

This repository has been forked from the Imgur upload repository, all credits to them
https://github.com/OttoAllmendinger/gnome-shell-imgur

