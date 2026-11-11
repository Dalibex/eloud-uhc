# Changelog

All notable changes to UHC ELOUD are documented in this file.

## [Unreleased]

## [1.5.4] - 2026-09-27

Smoother hosted matches, clearer administration and three new languages. Builds for Minecraft 26.2 and 26.3.

### Added

- French, German and Italian, next to Spanish and English. Each player picks a language with `/lang`.
- `/uhccommands` opens an interactive chat menu with the player and admin commands apart.
- Each episode shulker has its own episode selector (1-10) in the Admin Panel, and both can use the same episode.
- Rescue boat: a player scattered onto a rescue glass block over water receives a boat.
- Skin rotation can be turned off in the Admin Panel (*General Rules* > *Skin Rotation*). It is on by default and can only be changed in the lobby.
- `skins.fallback-roster` in `config.yml`: public accounts used as extra skin sources, so players without a skin of their own still get a unique identity.
- Short protection and regeneration at match start, against accidental damage from the scatter.

### Changed

- Skin rotation in episode 1 starts sooner and applies identities faster.
- Player skins are loaded when players join and when the match roster is prepared, so identity rotation and death heads are ready sooner.
- The chunks around the scatter points are loaded before players are teleported, which reduces lag at match start. Pregenerating the world up to the border is still recommended for real matches.
- Tablist names and nametags refresh one player at a time at match start, at chapter changes and on `/reset`, so TAB animations no longer freeze.
- With 1.8 combat on, axes deal legacy damage: 6 for diamond and 7 for netherite.
- World game rules can be changed from the Admin Panel during a match, not only in the lobby.
- The shulker toggles sit next to their episode selectors in the Shulkers panel.
- The dependency check and the startup banner print clear status lines in the console.

### Fixed

- TAB player-list health is created when needed and refreshed after the match starts and when a player reconnects.
- PVP turns on at match start when the PVP episode is 1.
- Shulker, PVP episode, team episode and skin rotation settings lock once the match starts. 1.8 combat and the offhand/shield lock can still be changed during the match.
- Death heads look for a safer place, for example under water, and drop as an item when they cannot be placed.
- The rescue boat message shows the plugin prefix instead of a raw `%prefix%`.
- `/reset` brings back real names in the tablist and nametags at once, with no fake identities left from the previous match.
- Skins are applied correctly when players join, at match start and during the match.

## [1.5.3] - 2026-09-22

First version numbered without `-SNAPSHOT`. It needs Minecraft 26.2, Java 25, TAB and SkinsRestorer.

### Added

- Team formation episode (1-10): the episode when teams are formed and ally compasses are given. Set it in the Admin Panel (*General Rules* > *Team Formation Episode*) or with `/setteamepisode <1-10>`.
- PVP episode (1-10): the episode when the gentleman's pact ends. Set it in the Admin Panel (*General Rules* > *PVP Episode*) or with `/setpvpepisode <1-10>`.
- `/abandon [player]`: leave the match, or, as an admin, mark another player as eliminated, online or offline.
- Tab completion for every command.
- `tab.setup-mode` in `config.yml` (`off`, `once` or `force`) decides whether the plugin writes the TAB configuration.

### Changed

- Requires Minecraft 26.2 and Java 25 (before: Minecraft 1.21.11 and Java 21).
- TAB and SkinsRestorer are required: the plugin does not start without them.
- The Admin Panel has its own submenus for shulkers, team episode, PVP episode, game rules, border and time.
- `/tpartes` is now `/settime`.
- Skins rotate in turns to avoid lag: the first players 10 seconds after the chapter change, then one player every 5 seconds.
- A player in combat gets the new skin after the fight, or skips that rotation if the fight lasts too long.
- A revealed identity stays revealed until the end of the episode; survivors get a new identity at the next rotation.
- Global chat during a match is anonymous (`[GLOBAL] message`), so the readable text no longer shakes next to obfuscated names.
- `/assignteam` accepts colors as shown (`red`, `RED`) or with the internal prefix (`h_red`), and suggests plain colors.
- The ally compass shows the teammate's name and distance in the action bar every second, in the main hand or the off-hand.

### Fixed

- Players who are offline during a skin rotation keep their turn, and their identity is resynchronized when they reconnect.
- `/reset` brings back real skins and keeps the custom teams and the players selected in them.
- The ally compass keeps pointing at the teammate after a skin or TAB refresh, instead of pointing at 0, 0.
- Team membership no longer breaks when TAB reorders scoreboard teams.
- Cancelling the start no longer leaves the skin rotation half applied.
- Resource Rush: objectives count only items really picked up or crafted, offline players keep their progress, a single player can win, and teams form correctly in episode 1.

### Security

- The plugin only manages its own scoreboard teams (prefix `h_`) and never deletes or changes teams of other plugins. Teams from older versions are migrated once.
- Admin menus require the admin permission and block clicks and drags that could take their items.

## [1.4.5-SNAPSHOT] - 2025-12-29

### Changed

- Random teams spread living players evenly. With 7 players alive for 4 teams, the teams get 2, 2, 2 and 1 living players, and eliminated players fill the rest.
- Spanish and English messages reviewed for consistent wording and colors.

### Fixed

- Commands reject negative numbers, letters in numeric arguments and borders under 20 blocks.
- *Cancel* in the `/start` confirmation cancels the start.
- `/tpartes`, `/lang` and `/start` are blocked once the match has started.

## [1.4.4-SNAPSHOT] - 2025-12-29

### Fixed

- When every player but one dies before the teams are formed, that player wins.

## [1.4.3-SNAPSHOT] - 2025-12-28

### Added

- Supply shulker boxes in episodes 1 and 8. They can be turned off in the Admin Panel.
- The victory message lists every member of the winning team, with fallen teammates struck through in gray.
- Winners get Resistance and instant health during the celebration.

### Changed

- `/reset` teleports every player to the spawn (0, 0) and clears inventories and the previous victory.
- Natural health regeneration is turned off in every world at match start.

### Fixed

- A death before the teams were formed ended the match without a winner.
- TAB health shows correctly from the start of the match.

## [1.3.1-SNAPSHOT] - 2025-12-25

### Added

- Golden heads: players leave their head on a fence where they die. A head surrounded by 8 gold ingots crafts a golden head, which gives Regeneration II for 12 seconds and Absorption II for 5 minutes.
- Locator bar option in the game rules of the Admin Panel.
- `/tpartes <h> <m> <s>` sets the chapter duration.
- Lobby standby after `/reset`: players are in adventure mode, invulnerable and never hungry. The countdown removes these effects and switches players to survival.

### Fixed

- The team compass follows the nearest teammate on its own.

## [1.2.0-SNAPSHOT] - 2025-12-24

### Added

- 1.8-style combat: no attack cooldown, no sweep attack and rebalanced axe damage.
- Shield and offhand lock, which also blocks shift-click, the swap key and dragging items into the off-hand.
- Victory detection for the last team alive, with fireworks, sounds and a sidebar that shows the winning team.

### Fixed

- The scatter no longer places players underground at negative coordinates or on snow.
- A player scattered onto water or lava gets a glass platform right below them.
- Chat colors are easier to read, team chat works for a player alone, and messages are no longer duplicated.

## [1.1.0-SNAPSHOT] - 2025-12-23

First version, for Paper 1.21.11.

### Added

- Admin Panel (`/uhcadmin`) for the border, chapter time, teams and game rules, also during a match.
- Even scatter of the players inside the border.

[Unreleased]: https://github.com/Dalibex/eloud-uhc/compare/v1.5.4...HEAD
[1.5.4]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.5.4
[1.5.3]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.5.3
[1.4.5-SNAPSHOT]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.4.5-SNAPSHOT
[1.4.4-SNAPSHOT]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.4.4-SNAPSHOT
[1.4.3-SNAPSHOT]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.4.3-SNAPSHOT
[1.3.1-SNAPSHOT]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.3.1-SNAPSHOT
[1.2.0-SNAPSHOT]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.2.0-SNAPSHOT
[1.1.0-SNAPSHOT]: https://github.com/Dalibex/eloud-uhc/releases/tag/v1.1.0-SNAPSHOT
