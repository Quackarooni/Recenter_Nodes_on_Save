# Recenter Nodes on Save

An addon that centers all nodetrees at (0,0) in basic node editors *(shaders, geometry nodes, compositing, texture nodes)* upon saving.  

## Installation

Download the .zip file from the release page and install via `Edit > Preferences > Addons > Install`. Blender should automatically recognize the file as an add-on.

## Usage

Once the addon is installed and enabled, recentering should happen every time a blendfile is saved. No hotkeys or buttons need to be toggled, it should do everything automatically. *(It's worth noting that the addon only changes the node positions, it cannot adjust the Node Editors current view to frame the nodes in their new location.)*

---

## Preferences

<img title="" src="https://user-images.githubusercontent.com/83491032/216546352-69e6bbae-94d0-4c6b-993e-b45f1a94de10.png" alt="preferences" data-align="inline">

#### - Debug Messages:

    Toggles what gets printed to the system console during the process.

> `None` - No messages are printed to system console.
> 
> `Minimal` - Prints out successful recentering operations.
> 
> `All` - Prints out both successful and cancelled recentering operations.
