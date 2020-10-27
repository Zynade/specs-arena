# __Specs Arena__

Specs Arena is a program used to access, view and store technical specifications of various mobile phone, tablet, and other handheld gadgets. It offers a convenient graphical user interface for comfortable, quick and easy use.

[Screenshots](https://imgur.com/a/ZckEmdB)

## __Features__

-View details of all mobile devices,

-Search for any specific device with several filter options,

-Submit details of a new device,

-Modify a device,

-Delete the details of a device

## __Usage__

There are two ways to run Specs Arena.
1) Run the **specs_arena.exe** executable. This can be found in the [Releases](https://github.com/Zynade/specs-arena/releases) section. However in some cases, Windows might flag this as malware due to the executable nature. If this occurs, you can make an exclusion for this folder in [Windows Security settings](https://support.microsoft.com/en-us/help/4028485/windows-10-add-an-exclusion-to-windows-security). Alternatively,
    
2) Run the **specs_arena.py** file. You must install the ```PIL``` dependency for the program to be fully functional however. This can be done by opening Powershell/Terminal and typing ```py -m pip install pillow```.



## __Instructions__

    Some general shortcuts:

-TAB/ENTER allows you to proceed to the next field in Write, Add, Update, and Delete Device.

-ESC allows you to go back to homescreen from any page.

-The arrow keys can also be utilized to scroll up or down the pages, in addition to mouse wheel.

        
    Display All Devices:
-Displays information about all stored devices. Scroll up and down using mouse wheel, or the UP and DOWN arrow keys.


    Write Device:	
-Enter the required information about the device, and select an image using the Browse Image File button. As of right now, only JPEG images are supported.

-Click the Write Device button.

-Note: This will completely overwrite ALL existing records. Proceed at your own risk.


    Add Device:
-Enter the required information about the device, and select an image using the Browse Image button. As of right now, only JPEG images are supported.

-Click the Add Device button.

-This will add the device to the database. No data will be overwritten.


    Update Device:
-This allows you to update the information of a device from the database.

-After entering all required information, click the Edit button and then Browse Image File to attach new image.

-Click the Update Device button.


    Delete Device:
-Enter all details of the device you wish to delete and click Delete Device.


    Search Device:
-Allows you to search and browse through information of any desired device.

-You have several options to filter the search results, including but not limited to: search by Manufacturer, Name, Screen Resolution, Chipset etc.
        

    About:
-Displays some basic information about Specs Arena.



## __Some common issues__

- > "I see 0 records found in the Display All Devices tab!" 
 
->>> Make sure `devices.dat` is in the same directory as specs_arena.exe and specs_arena.py. If you are running the .py and this issue still persists, you should open the Specs Arena folder in your IDE, rather than just the .py file.

## License

This program is available under the GNU GPLv3 license.
Please refer to COPYING for more information.
