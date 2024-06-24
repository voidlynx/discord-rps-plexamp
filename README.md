# Discord Rich Presence for Plexamp

![Showcase](https://i.imgur.com/oBtnoIP.png)

Discord Rich Presence for Plexamp is a Python script that displays your [Plex](https://www.plex.tv/) status on [Discord](https://discord.com/) using [Rich Presence](https://discord.com/developers/docs/rich-presence/how-to).

## Usage

1. Install [Python](https://www.python.org/downloads/) - Make sure to tick "Add Python 3.XX to PATH" during the installation.
2. Download [this repository's contents](https://github.com/voidlynx/discord-rps-plexamp/archive/refs/heads/master.zip).
3. Extract the folder contained in the above ZIP file.
4. Launch the `start.bat` file.
5. Install the required Python modules by running `pip install -U -r requirements.txt`.
6. Start the script by running `python main.py`.

When the script runs for the first time, a `config.json` file will be created in the working directory and you will be prompted to complete the authentication flow to allow the script to retrieve an access token for your Plex account.

The script must be running on the same machine as your Discord client.

## Configuration - `config.json`

* `logging`
  * `debug` (boolean, default: `true`) - Outputs additional debug-helpful information to the console if enabled.
  * `writeToFile` (boolean, default: `false`) - Writes everything outputted to the console to a `console.log` file if enabled.
* `display` - Display settings for Rich Presence
  * `hideTotalTime` (boolean, default: `false`) - Hides the total duration of the media if enabled.
  * `useRemainingTime` (boolean, default: `false`) - Displays the media's remaining time instead of elapsed time if enabled.
  * `posters`
    * `enabled` (boolean, default: `false`) - Uses [cover-uploady](https://github.com/voidlynx/cover-uploady) to display a cover art. Requires setup of the two variables below. See [usage](#cover-uploady-usage).
    * `cuDomain` (string, default: `""`) - Domain that cover-uploady is hosted on. The `/upload` and `/cover.jpg` endpoints are automatically appended when required, don't worry.
    * `cuSecret` (string, default: `""`) - Cover-uploady's secret passphrase for uploads. See below.
  * `buttons` (list) - [Information](#buttons)
    * `label` (string) - The label to be displayed on the button.
    * `url` (string) - A web address or a [dynamic URL placeholder](#dynamic-button-urls).
* `users` (list)
  * `token` (string) - An access token associated with your Plex account. ([X-Plex-Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/), [Authenticating with Plex](https://forums.plex.tv/t/authenticating-with-plex/609370))
  * `servers` (list)
    * `name` (string) - Name of the Plex Media Server you wish to connect to.
    * `listenForUser` (string, optional) - The script will respond to alerts originating only from this username. Defaults to the parent user's username if not set.
    * `blacklistedLibraries` (list, optional) - Alerts originating from libraries in this list are ignored.
    * `whitelistedLibraries` (list, optional) - If set, alerts originating from libraries that are not in this list are ignored.

### Cover-Uploady usage
This fork uses a microservice called [cover-uploady](https://github.com/voidlynx/cover-uploady) to display the cover art image. This service should be self-hosted and is for advanced users. Sorry. The original fork spammed Imgur's API and that, honestly, was worse. 

1. Install [cover-uploady](https://github.com/voidlynx/cover-uploady).
2. When writing the .env file, write a SECRET string. It can be whatever you want and however long or short you want, but longer is better, I keep mine at 32 chars.
3. Copy the SECRET and insert it into `cuSecret` in the `config.json` file.
4. Copy the domain that the microservice is hosted on (like `cover.vlnx.ru` in my case) to the `cuDomain` variable.
5. Don't forget to switch `display.posters.enabled` to `true`! 

### Buttons

Discord can display up to 2 buttons in your Rich Presence.

Due to a strange Discord bug, these buttons are unresponsive or exhibit strange behaviour towards your own clicks, but other users are able to click on them to open their corresponding URLs. (citation needed)

Please don't abuse this as another funny field. Link to something worthwhile, don't just use it as an extra place to post your whatever.

#### Dynamic Button URLs

During runtime, the following dynamic URL placeholders will get replaced with real URLs based on the media being played:
* `dynamic:imdb`
* `dynamic:tmdb`

### Example

```json
{
  "logging": {
    "debug": true,
    "writeToFile": false
  },
  "display": {
    "hideTotalTime": false,
    "useRemainingTime": false,
    "posters": {
      "enabled": true,
      "cuDomain": "cover.example.com",
      "cuSecret": "9e9sf637S8bRp4z"
    },
    "buttons": [
      {
        "label": "IMDb Link",
        "url": "dynamic:imdb"
      },
      {
        "label": "My YouTube Channel",
        "url": "https://www.youtube.com/channel/me"
      }
    ]
  },
  "users": [
    {
      "token": "HPbrz2NhfLRjU888Rrdt",
      "servers": [
        {
          "name": "Bob's Home Media Server"
        },
        {
          "name": "A Friend's Server",
          "listenForUser": "xyz",
          "whitelistedLibraries": ["Movies"]
        }
      ]
    }
  ]
}
```

## Configuration - Discord

The "Display current activity as a status message" setting must be enabled in Discord Settings → Activity Settings → Activity Privacy.

![Discord Settings](https://user-images.githubusercontent.com/59180111/186830889-35af3895-ece0-4a7d-9efb-f68640116884.png)
