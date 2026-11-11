# ⚔️ UHC ELOUD

[![Release](https://img.shields.io/github/v/release/Dalibex/eloud-uhc?sort=semver)](https://github.com/Dalibex/eloud-uhc/releases/latest)
[![Minecraft](https://img.shields.io/modrinth/game-versions/uhc-eloud?label=Minecraft)](https://modrinth.com/plugin/uhc-eloud/versions)
[![Modrinth downloads](https://img.shields.io/modrinth/dt/uhc-eloud?logo=modrinth&label=Modrinth)](https://modrinth.com/plugin/uhc-eloud)
[![CurseForge downloads](https://img.shields.io/curseforge/dt/1413639?logo=curseforge&label=CurseForge)](https://www.curseforge.com/minecraft/bukkit-plugins/uhc-eloud)
[![License](https://img.shields.io/badge/license-PolyForm%20Noncommercial%201.0.0-blue)](LICENSE)

UHC ELOUD is a Paper plugin for hosting UHC matches, inspired by **UHC ESPAÑA** by **ElRichMC**. It runs the whole match: setup from an admin panel, scatter, chapters, teams, fake identities, supplies and the victory.

What changed in each version is in the [changelog](CHANGELOG.md).

## 🎮 Features

- **Match flow:** `/reset` prepares the lobby, `/start` scatters the players after a confirmation, and the match runs in chapters up to the victory.
- **Game modes:**
  - **Classic UHC:** the last team or player standing wins.
  - **Resource Rush:** each episode reveals random items to collect, up to 12. Teams are ranked on a podium in the order they collect all of them, and the first one wins.
- **Admin Panel:** game mode, chapter time, border, game rules, teams, PVP episode, team episode and supply shulkers, from one menu.
- **Teams:** solos or teams, random or chosen with a team selector, assigned by an admin, and formed in the episode you choose.
- **Fake identities:** players get another player's skin and name every chapter, revealed by hitting them, and drop a head with their real skin when they die. Uses SkinsRestorer.
- **Supplies:** shulker boxes in the episodes you choose, golden heads, team compasses and a boat when the scatter lands a player on water.
- **Combat options:** 1.8-style combat (no attack cooldown, no sweep attack, legacy axe damage) and an offhand and shield lock.
- **Player interface:** sidebar, health in the player list, and tablist names and nametags that follow the fake identities. Uses TAB.
- **Languages:** Spanish, English, French, German and Italian. Each player picks one with `/lang`.

## 🧰 Requirements

- A [Paper](https://papermc.io/) or Purpur server. The supported Minecraft versions are listed on each [download](https://modrinth.com/plugin/uhc-eloud/versions).
- Java 25 or newer.
- [TAB](https://github.com/NEZNAMY/TAB/releases) and [SkinsRestorer](https://github.com/SkinsRestorer/SkinsRestorer/releases). Both are required: the plugin does not start without them.

## 📥 Installation

1. Download the plugin from [Modrinth](https://modrinth.com/plugin/uhc-eloud), [CurseForge](https://www.curseforge.com/minecraft/bukkit-plugins/uhc-eloud) or the [GitHub releases](https://github.com/Dalibex/eloud-uhc/releases).
2. Put it in the `plugins/` folder of the server, together with TAB and SkinsRestorer.
3. Start the server. The console shows whether both dependencies were found.

Each GitHub release also has a server pack (`UHC_ELOUD_<version>_MC<minecraft>.zip`) per Minecraft version: a prepared server folder with links to download Paper, TAB and SkinsRestorer.

## 📋 Hosting A Match

1. Run `/reset`. Players wait in the lobby in adventure mode, without taking damage.
2. Change the chapter length with `/settime <h> <m> <s>` if 20 minutes is not what you want.
3. Open `/uhcadmin` and choose the game mode, teams, PVP episode, team episode, shulkers, game rules and border.
4. Run `/start <size>` with the border size in blocks, and confirm with the button in chat.

> [!TIP]
> Pregenerate the world up to the border before a real match. Loading chunks during the scatter causes lag.

Admin Panel settings last until the server restarts.

## ⌨️ Commands

*Admin* means operators, or players with the `uhc.admin` permission.

| Command | What it does | Who |
| :-- | :-- | :-- |
| `/uhccommands` | Lists the commands in an interactive chat menu. | Everyone |
| `/lang <es\|en\|fr\|de\|it>` | Changes your language. Only in the lobby. | Everyone |
| `/team <name>` | Renames your team. | Everyone |
| `/abandon [player]` | Leaves the match. An admin can name another player, online or offline, to eliminate them. | Everyone |
| `/uhcadmin` | Opens the Admin Panel. | Admin |
| `/reset` | Resets the match and prepares the lobby. | Admin |
| `/start <size>` | Starts the match with a border of `<size>` blocks, at least 20, after a confirmation. | Admin |
| `/confirmstart`, `/cancelstart` | Run by the buttons of the `/start` confirmation. You do not need to type them. | Admin |
| `/settime <h> <m> <s>` | Sets the chapter length. Only in the lobby. | Admin |
| `/assignteam <player> <team>` | Puts a player in a team. | Admin |
| `/setteamepisode <1-10>` | Sets the episode when teams are formed. | Admin |
| `/setpvpepisode <1-10>` | Sets the episode when PVP starts. | Admin |

## ⚙️ Configuration

The plugin creates `plugins/ELOUD_UHC/config.yml` on the first start.

| Key | What it does | Default |
| :-- | :-- | :-- |
| `language` | Language of players who have not chosen one with `/lang`: `es`, `en`, `fr`, `de` or `it`. | `en` |
| `tab.setup-mode` | Whether the plugin writes TAB's `config.yml` and `animations.yml`: `off` never, `once` on the first start, `force` on every start. Use `off` if you keep your own TAB configuration. | `once` |
| `skins.fallback-roster` | Public accounts used as extra skins when the players do not have enough different skins. | A list of known players |

`tab.setup-completed` and `migrations` are written by the plugin. Set `tab.setup-completed` back to `false` to let `once` write the TAB files again. The language each player chose is saved in `player_langs.yml`.

## 🛠️ Building From Source

You need JDK 25. Gradle is downloaded by the wrapper.

```bash
./gradlew clean test jar
```

On Windows, use `gradlew.bat`. The plugin is written to `build/libs/ELOUD_UHC-<version>.jar`. `./gradlew runServer` starts a local test server, which also needs TAB and SkinsRestorer in `run/plugins/`.

## 💬 Support

- Bugs and ideas: open an [issue](https://github.com/Dalibex/eloud-uhc/issues/new/choose). [CONTRIBUTING.md](CONTRIBUTING.md) explains what to include.
- Questions about installing or hosting: use [Discussions](https://github.com/Dalibex/eloud-uhc/discussions/categories/q-a).
- Security problems: report them privately as described in [SECURITY.md](SECURITY.md).

## 📄 License

UHC ELOUD is licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE). It allows using, changing and sharing the plugin for noncommercial purposes. Any other use needs the author's permission.
